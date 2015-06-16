
#ifndef ConverterRunOne_h
#define ConverterRunOne_h

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <memory>

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>

// mut_dataformats includes
#include "mut_framework/mut_dataformats/interface/EventInfo.h"
#include "mut_framework/mut_dataformats/interface/Lepton.h"
#include "mut_framework/mut_dataformats/interface/Jet.h"
#include "mut_framework/mut_dataformats/interface/MET.h"



class ConverterRunOne : public TSelector {
  public :

    // asociated with a TTree 
    TTreeReader reader;

    // TreeReader pointers for event information
    TTreeReaderValue<double> event; 
    TTreeReaderValue<int> lumi;
    TTreeReaderValue<int> run; 
    TTreeReaderValue<int> nPV;
    TTreeReaderValue<int> goodLumi;


    // Vectors of TTreeReaders pointers to jet variables
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> pfjet_energy;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> pfjet_eta;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> pfjet_phi;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> pfjet_pt;
    std::vector<std::unique_ptr<TTreeReaderValue<int>>> jet_flavour;
    std::vector<std::vector<std::pair<std::string,std::unique_ptr<TTreeReaderValue<double>>>>> pfjet_disc;

    // Vector of discriminator names to attach to each jet
    std::vector<std::string> disc_names;

    // Vectors of TTreeReader pointers to muon variables
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> muon_energy;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> muon_eta;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> muon_phi;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> muon_pt;
    std::vector<std::unique_ptr<TTreeReaderValue<double>>> muon_relIso;

    // TreeReader pointer to MET variables
    TTreeReaderValue<double> pf_met_pt;
    TTreeReaderValue<double> pf_met_px;
    TTreeReaderValue<double> pf_met_py;

    // maximum number of jets to consider 
    int n_pfjet = 7;
     // maximum number of muons to consider
    int n_muon = 1;

    // output filename
    std::string o_filename;

    // mut objects to save to TTree
    mut::EventInfo * eventInfo = nullptr;
    std::vector<mut::Jet> * pfjets = nullptr;
    std::vector<mut::Lepton> * muons = nullptr;
    mut::MET * pfmet = nullptr;

    // TTree pointer
    TTree * ttree;

    // default constructor
    ConverterRunOne(TTree * /*tree*/ =0) : 
     event(reader,"event_mu"), 
     lumi(reader, "lumi_mu"),
     run(reader, "run_mu"),
     nPV(reader, "nPV_mu"),
     goodLumi(reader, "GoodLumi_mu"),
     pf_met_pt(reader,"PF_met_pt_mu"),
     pf_met_px(reader,"PF_met_px_mu"),
     pf_met_py(reader,"PF_met_py_mu")
{}

   // destructor
   virtual ~ConverterRunOne()  { }

   // TSelector functions
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();


};

#endif

#ifdef ConverterRunOne_cxx

// each new tree is opened
void ConverterRunOne::Init(TTree *tree)
{
  reader.SetTree(tree);
}

// each new file is opened
Bool_t ConverterRunOne::Notify()
{

   return kTRUE;
}

#endif // #ifdef ConverterRunOne_cxx
