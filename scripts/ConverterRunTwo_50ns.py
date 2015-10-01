#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunTwo
from os.path import split

folder_dir = "/user_data/pdecastr/BTagSF/Samples/13TeV/LJMet_METnoHFplusHTT_092515/"

data_names = [["SingleMuon_PR", {"min_run" : 251585, "max_run": 251883 }],
              ["SingleMuon_RR", {"min_run" : 251162, "max_run": 251562 }]]
              
              

mc_names = ["TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_50ns",
            "WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_50ns",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_50ns",
            "ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_50ns",
            "ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_50ns",
            "ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_50ns",
            "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_50ns",
            "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_50ns",
            "WW_TuneCUETP8M1_13TeV-pythia8_50ns",
            "WZ_TuneCUETP8M1_13TeV-pythia8_50ns" ]
         


o_dir = "/user_data/pdecastr/BTagSF/BetterTTrees/13TeV_50ns/"              

rootnames = mc_names + data_names


for name in mc_names:
    converter = ConverterRunTwo()
    outfile = o_dir+name+".root" 
    tchain = TChain("ljmet")
    wildcard_name = folder_dir + name + "/" + name + "*.root"
    print "Processing all files with wildcard:  {} ".format(wildcard_name)
    n_files = tchain.Add(wildcard_name)
    print "Added {} files to TChain".format(n_files)
    tchain.Process(converter,"ofile="+outfile)

for name in data_names:
    converter = ConverterRunTwo()
    for k,v in name[1].items():
        setattr(converter,k,v)
    outfile = o_dir+name[0]+".root" 
    tchain = TChain("ljmet")
    wildcard_name = folder_dir + name[0] + "/" + name[0] + "*.root"
    print "Processing all files with wildcard:  {} ".format(wildcard_name)
    n_files = tchain.Add(wildcard_name)
    print "Added {} files to TChain".format(n_files)
    tchain.Process(converter,"ofile="+outfile)
