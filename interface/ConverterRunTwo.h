
#ifndef ConverterRunTwo_h
#define ConverterRunTwo_h

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <memory>
#include <limits>

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



class ConverterRunTwo : public TSelector {
  public :

    long n_entries;

    // asociated with a TTree 
    TTreeReader reader;

    // TreeReader pointers for event information
    TTreeReaderValue<int> event; 
    TTreeReaderValue<int> lumi;
    TTreeReaderValue<int> run; 
    TTreeReaderValue<int> nPV;
    // event MC weight (can be negative)
    TTreeReaderValue<double> MCweight;

    // to be able to filter by run
    int min_run = std::numeric_limits<int>::min();
    int max_run = std::numeric_limits<int>::max();

    // Vectors of TTreeReaders vectors
    TTreeReaderValue<std::vector<double>> pfjet_energy;
    TTreeReaderValue<std::vector<double>> pfjet_eta;
    TTreeReaderValue<std::vector<double>> pfjet_phi;
    TTreeReaderValue<std::vector<double>> pfjet_pt;
    TTreeReaderValue<std::vector<int>> jet_flavour;
    std::vector<std::pair<std::string,std::unique_ptr<TTreeReaderValue<std::vector<double>>>>> pfjet_disc;
    // Vector of discriminator names to attach to each jet
    std::vector<std::string> disc_names;

    // TTreeReaders to muon variables
    TTreeReaderValue<std::vector<double>> muon_energy;
    TTreeReaderValue<std::vector<double>> muon_eta;
    TTreeReaderValue<std::vector<double>> muon_phi;
    TTreeReaderValue<std::vector<double>> muon_pt;
    TTreeReaderValue<std::vector<double>> muon_relIso;
    TTreeReaderValue<std::vector<int>> muon_charge;

    // TTreeReaders to elec variables
    TTreeReaderValue<std::vector<double>> elec_energy;
    TTreeReaderValue<std::vector<double>> elec_eta;
    TTreeReaderValue<std::vector<double>> elec_phi;
    TTreeReaderValue<std::vector<double>> elec_pt;
    TTreeReaderValue<std::vector<double>> elec_relIso;
    TTreeReaderValue<std::vector<int>> elec_charge;

    // TreeReader pointer to MET variables
    TTreeReaderValue<double> pf_met_energy;
    TTreeReaderValue<double> pf_met_phi;

    // output filename
    std::string o_filename;

    // mut objects to save to TTree
    mut::EventInfo * eventInfo = nullptr;
    std::vector<mut::Jet> * pfjets = nullptr;
    std::vector<mut::Lepton> * muons = nullptr;
    std::vector<mut::Lepton> * elecs = nullptr;
    mut::MET * pfmet = nullptr;

    // TTree pointer
    TTree * ttree;
    // TFile poinyer
    TFile * o_file;

    // configuration
    bool hasBTagSFCalc = false; 

    // default constructor
    ConverterRunTwo(TTree * /*tree*/ =0) : 
     event(reader,"event_CommonCalc"), 
     lumi(reader, "lumi_CommonCalc"),
     run(reader, "run_CommonCalc"),
     nPV(reader, "nPV_singleLepCalc"),
     MCweight(reader, "MCWeight_singleLepCalc"),
     pfjet_energy(reader,"theJetEnergy_JetSubCalc"),
     pfjet_eta(reader,"theJetEta_JetSubCalc"),
     pfjet_phi(reader,"theJetPhi_JetSubCalc"),
     pfjet_pt(reader,"theJetPt_JetSubCalc"),
     jet_flavour(reader,"theJetFlav_JetSubCalc"),
     muon_energy(reader,"muEnergy_singleLepCalc"),
     muon_eta(reader,"muEta_singleLepCalc"),
     muon_phi(reader,"muPhi_singleLepCalc"),
     muon_pt(reader,"muPt_singleLepCalc"),
     muon_relIso(reader,"muRelIso_singleLepCalc"),
     muon_charge(reader,"muCharge_singleLepCalc"),
     elec_energy(reader,"elEnergy_singleLepCalc"),
     elec_eta(reader,"elEta_singleLepCalc"),
     elec_phi(reader,"elPhi_singleLepCalc"),
     elec_pt(reader,"elPt_singleLepCalc"),
     elec_relIso(reader,"elRelIso_singleLepCalc"),
     elec_charge(reader,"elCharge_singleLepCalc"),
     pf_met_energy(reader,"corr_met_singleLepCalc"),
     pf_met_phi(reader,"corr_met_phi_singleLepCalc")
{}

   // destructor
   virtual ~ConverterRunTwo()  { }

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

#ifdef ConverterRunTwo_cxx

// each new tree is opened
void ConverterRunTwo::Init(TTree *tree)
{
  reader.SetTree(tree);
}

// each new file is opened
Bool_t ConverterRunTwo::Notify()
{

   return kTRUE;
}

#endif // #ifdef ConverterRunTwo_cxx
