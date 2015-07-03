#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunOne
from os.path import split

file_dir = "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/"

data = ["Data_2012ABCD_Winter13_ReReco.root"]

mc_bn = ["TTbar_{}Summer13.root",
         "T_t_{}Summer13.root",
         "Tbar_t_{}Summer13.root",
         "T_tW_{}_Summer13.root",
         "Tbar_tW_{}Summer13.root",
         "WJets_{}Summer13.root",
         "ZJets_{}Summer13.root"]

nom_samples = [s.format("") for s in mc_bn]
ttbar_s = [s.format("SUP_") for s in mc_bn[0:1]] + [s.format("SDOWN_") for s in mc_bn[0:1]]
ttbar_m= [s.format("MUP_") for s in mc_bn[0:1]] + [s.format("MDOWN_") for s in mc_bn[0:1]]
jec_samples = [s.format("JEC_UP_") for s in mc_bn] + [s.format("JEC_DOWN_") for s in mc_bn]
jer_samples = [s.format("JER_UP_") for s in mc_bn] + [s.format("JER_DOWN_") for s in mc_bn]

o_dir = "/user_data/pdecastr/BTagSF/BetterTTrees/"              
outfiles = []

rootfiles = nom_samples + ttbar_s + ttbar_m + jec_samples + jer_samples + data


for f in rootfiles:
    print "Converting file:" + f
    converter = ConverterRunOne()
    outfiles.append(o_dir+split(f)[1]) 
    tchain = TChain("treetop_mu")
    tchain.Add(file_dir + f)
    tchain.Process(converter,"ofile="+outfiles[-1])


    
    
