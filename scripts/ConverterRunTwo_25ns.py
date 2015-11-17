#!/usr/bin/env python 

import ROOT
from ROOT import TChain, ConverterRunTwo
from os.path import split

folder_dir = "/user_data/pdecastr/BTagSF/Samples/13TeV/LJMet_1lep_110415/nominal/"

data_names = [["SingleMuon_RRC_25ns",{}],
              ["SingleMuon_PRD_25ns",{}],
              ["SingleMuon_RRD_25ns", {}]]

mc_names = ["TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_25ns",
            "WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_25ns",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_25ns",
            "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_25ns",
            "ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_25ns",
            "ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_25ns",
            "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_25ns",
            "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_25ns",
            "WW_TuneCUETP8M1_13TeV-pythia8_25ns",
            "WZ_TuneCUETP8M1_13TeV-pythia8_25ns",
            "TT_TuneCUETP8M1_13TeV-powheg-pythia8"]

qcd_names = ["QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns",
             "QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_25ns"]

wjet_names = ["WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns",
              "WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_25ns",
              "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_25ns"]

mc_names = mc_names + qcd_names + wjet_names 
o_dir = "/user_data/pdecastr/BTagSF/BetterTTrees/13TeV_25ns/"              

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
