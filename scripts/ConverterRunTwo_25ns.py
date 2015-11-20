#!/usr/bin/env python 

from mut_framework.LJMET_converter.samples_25ns import data_samples,mc_samples
from mut_framework.LJMET_converter.pu_weight import pu_weight
from mut_framework.LJMET_converter.pileup_25ns import pu_dists
from ROOT import TChain, ConverterRunTwo
import  os
import argparse


default_input_dir = "/user_data/pdecastr/BTagSF/Samples/13TeV/LJMet_1lep_110915/"
default_output_dir = "/user_data/pdecastr/BTagSF/mut_ttrees/13TeV_25ns/from_ljmet/" 

parser = argparse.ArgumentParser(description='integers.')
parser.add_argument('--input_folder', default=default_input_dir, type=str)
parser.add_argument('--output_folder', default=default_output_dir, type=str)
parser.add_argument('--mc_samples', default=[], nargs='*')
parser.add_argument('--data_samples', default=[], nargs='*')
parser.add_argument('--all_samples', action="store_true")
args = parser.parse_args()

i_folder = args.input_folder
o_folder = args.output_folder

# pu weights to apply
pu_w = {
        "pileup_nom"  : pu_weight(pu_dists["data_69000mb"],pu_dists["winter15_MC"]),
        "pileup_up"   : pu_weight(pu_dists["data_72450mb"],pu_dists["winter15_MC"]),
        "pileup_down" : pu_weight(pu_dists["data_65550mb"],pu_dists["winter15_MC"])
       }




if not os.path.exists(o_folder):
        os.makedirs(o_folder)

if args.all_samples:
    mc_names = mc_samples.keys()
    data_names = data_samples.keys()
else:
    mc_names = args.mc_samples
    data_names = args.data_samples

for name in mc_names:
    converter = ConverterRunTwo()
    for k,v in pu_w.items():
        converter.add_pu_weight(k,v)
    full_name = mc_samples[name]["full_name"]
    outfile = o_folder+full_name+".root" 
    tchain = TChain("ljmet")
    wildcard_name = i_folder + full_name + "/" + full_name + "*.root"
    print "Processing all files with wildcard:  {} ".format(wildcard_name)
    n_files = tchain.Add(wildcard_name)
    print "Added {} files to TChain".format(n_files)
    tchain.Process(converter,"ofile="+outfile)

for name in data_names:
    converter = ConverterRunTwo()
    full_name = data_samples[name]["full_name"]
    outfile = o_folder+full_name+".root" 
    tchain = TChain("ljmet")
    wildcard_name = i_folder + full_name + "/" + full_name + "*.root"
    print "Processing all files with wildcard:  {} ".format(wildcard_name)
    n_files = tchain.Add(wildcard_name)
    print "Added {} files to TChain".format(n_files)
    tchain.Process(converter,"ofile="+outfile)
