#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunOne
from os.path import split

rootfiles = [ "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/TTbar_Summer13.root", 
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/T_t_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/Tbar_t_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/T_tW_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/Tbar_tW_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/WJets_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/ZJets_Summer13.root",
              "/user_data/pdecastr/BTagSF/Samples/8TeV/53x_Summer13/Data_2012ABCD_Winter13_ReReco.root"]

o_dir = "/user_data/pdecastr/BTagSF/BetterTTrees/"              
outfiles = []


for f in rootfiles:
    converter = ConverterRunOne()
    outfiles.append(o_dir+split(f)[1]) 
    tchain = TChain("treetop_mu")
    tchain.Add(f)
    tchain.Process(converter,"ofile="+outfiles[-1])


    
    
