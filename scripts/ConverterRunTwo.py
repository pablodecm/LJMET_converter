#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunTwo
from os.path import split

file_dir = "/user_data/pdecastr/BTagSF/Samples/13TeV/bTag_noHF_Combined/"

data = ["Single_el_Prompt.root",
        "Single_el_Rereco.root",
        "Single_mu_Prompt.root",
        "Single_mu_Rereco.root"]

mc_bn = ["QCD_1000to1400.root",
         "QCD_120to170.root",
         "QCD_1400to1800.root",
         "QCD_170to300.root",
         "QCD_1800to2400.root",
         "QCD_2400to3200.root",
         "QCD_300to470.root",
         "QCD_30to50.root",
         "QCD_3200toInf.root",
         "QCD_470to600.root",
         "QCD_50to80.root",
         "QCD_600to800.root",
         "QCD_800to1000.root",
         "QCD_80to120.root",
         "T_t_atop.root",
         "TTbar.root",
         "T_t_top.root",
         "T_tW_atop.root",
         "TTW.root",
         "T_tW_top.root",
         "TTZll.root",
         "TTZqq.root",
         "WJets.root",
         "WW.root",
         "WZ.root",
         "ZJets.root",
         "ZZ.root"]
         


o_dir = "/user_data/pdecastr/BTagSF/BetterTTrees/13TeV/"              
outfiles = []

rootfiles = mc_bn + data


for f in rootfiles:
    print "Converting file:" + f
    converter = ConverterRunTwo()
    outfiles.append(o_dir+split(f)[1]) 
    tchain = TChain("ljmet")
    tchain.Add(file_dir + f)
    tchain.Process(converter,"ofile="+outfiles[-1])

