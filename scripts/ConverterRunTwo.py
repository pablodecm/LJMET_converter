#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunTwo
from os.path import split

file_dir = "/user_data/pdecastr/BTagSF/Samples/13TeV/bTag_noHF_Combined/"

data = ["Single_el_Rereco.root"]

mc_bn = ["TTW.root"]
         


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

