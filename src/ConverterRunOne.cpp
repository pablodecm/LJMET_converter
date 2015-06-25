#define ConverterRunOne_cxx
#include "../interface/ConverterRunOne.h"

// start of query (executed on client)
void ConverterRunOne::Begin(TTree * /*tree*/)
{

   std::string option = GetOption();

   std::size_t i_ofile = option.find("ofile="); 
   if (i_ofile != std::string::npos) {
     std::size_t length = (option.find(";", i_ofile) -  option.find("=", i_ofile) - 1);
     o_filename = option.substr(option.find("=", i_ofile)+1 , length );
   } else {
     o_filename = "output.root";
   }

   std::cout << "Output filename: " << o_filename << std::endl;
}

// right after begin (executed on slave)
void ConverterRunOne::SlaveBegin(TTree * /*tree*/)
{

   TString option = GetOption();

  ttree = new TTree("tree","Physics Object based TTree");

  ttree->Branch("eventInfo","mut::EventInfo", &eventInfo, 64000,1);
  ttree->Branch("pfmet","mut::MET", &pfmet, 64000,1);
  ttree->Branch("pfjets","std::vector<mut::Jet>", &pfjets, 64000,1);
  ttree->Branch("muons","std::vector<mut::Lepton>", &muons, 64000,1);

  fOutput->Add(ttree);  

  
  disc_names.emplace_back("combinedInclusiveSecondaryVertexBJetTags"); 
  disc_names.emplace_back("combinedMVABJetTags"); 
  disc_names.emplace_back("combinedSecondaryVertexBJetTags"); 
  disc_names.emplace_back("combinedSecondaryVertexMVABJetTags"); 
  disc_names.emplace_back("jetBProbabilityBJetTags"); 
  disc_names.emplace_back("jetProbabilityBJetTags"); 
  disc_names.emplace_back("simpleSecondaryVertexBJetTags"); 
  disc_names.emplace_back("simpleSecondaryVertexHighEffBJetTags"); 
  disc_names.emplace_back("simpleSecondaryVertexHighPurBJetTags"); 
  disc_names.emplace_back("trackCountingHighEffBJetTags"); 
  disc_names.emplace_back("trackCountingHighPurBJetTags"); 

  // load all jet branches
  for (int i=0;i < n_pfjet;i++) {
    std::string n_pfjet_energy = "PFjet"+std::to_string(i)+"_energy_mu";
    pfjet_energy.emplace_back(new TTreeReaderValue<double>(reader,n_pfjet_energy.c_str()));
    std::string n_pfjet_eta = "PFjet"+std::to_string(i)+"_eta_mu";
    pfjet_eta.emplace_back(new TTreeReaderValue<double>(reader,n_pfjet_eta.c_str()));
    std::string n_pfjet_phi = "PFjet"+std::to_string(i)+"_phi_mu";
    pfjet_phi.emplace_back(new TTreeReaderValue<double>(reader,n_pfjet_phi.c_str()));
    std::string n_pfjet_pt = "PFjet"+std::to_string(i)+"_pt_mu";
    pfjet_pt.emplace_back(new TTreeReaderValue<double>(reader,n_pfjet_pt.c_str()));
    std::string n_jet_flavour = "jet"+std::to_string(i)+"_Flavour_mu";
    jet_flavour.emplace_back(new TTreeReaderValue<int>(reader,n_jet_flavour.c_str()));
    pfjet_disc.emplace_back(); // default construct
    for ( std::string disc_name : disc_names ) { 
      std::string b_name = "jet"+std::to_string(i)+"_"+disc_name+"_mu";
      pfjet_disc[i].emplace_back(disc_name, std::unique_ptr<TTreeReaderValue<double>>(new TTreeReaderValue<double>(reader,b_name.c_str())));
    }
  }

  std::cout << "Jet bracnches loaded" << std::endl;

  // load all muon branches
  for (int i=0;i < n_muon;i++) {
    std::string n_muon_energy = "muon"+std::to_string(i)+"_energy_mu";
    muon_energy.emplace_back(new TTreeReaderValue<double>(reader,n_muon_energy.c_str()));
    std::string n_muon_eta = "muon"+std::to_string(i)+"_eta_mu";
    muon_eta.emplace_back(new TTreeReaderValue<double>(reader,n_muon_eta.c_str()));
    std::string n_muon_phi = "muon"+std::to_string(i)+"_phi_mu";
    muon_phi.emplace_back(new TTreeReaderValue<double>(reader,n_muon_phi.c_str()));
    std::string n_muon_pt = "muon"+std::to_string(i)+"_pt_mu";
    muon_pt.emplace_back(new TTreeReaderValue<double>(reader,n_muon_pt.c_str()));
    std::string n_muon_relIso = "muon"+std::to_string(i)+"_relIso_mu";
    muon_relIso.emplace_back(new TTreeReaderValue<double>(reader,n_muon_relIso.c_str()));
  }


  std::cout << "Muon braches loaded" << std::endl;
}

// for each entry of the TTree
Bool_t ConverterRunOne::Process(Long64_t entry)
{

  // set TTreeReader entry
  reader.SetEntry(entry);

  // create and fill EventInfo
  eventInfo = new mut::EventInfo(int(*event), *lumi, *run);
  eventInfo->setNumPV(*nPV);
  std::vector<std::pair<std::string, bool>> filterPairs;
  filterPairs.emplace_back("goodLumi",bool(*goodLumi));
  eventInfo->setFilterPairs(filterPairs);
  std::vector<std::pair<std::string, float>> weightPairs;
  weightPairs.emplace_back("weight_PU_down", *weight_PU_down);
  weightPairs.emplace_back("weight_PU_nom", *weight_PU_nom);
  weightPairs.emplace_back("weight_PU_up", *weight_PU_up);
  eventInfo->setWeightPairs(weightPairs);

  // create and fill mut MET
  pfmet = new mut::MET();
  pfmet->SetPxPyPzE(*pf_met_px, *pf_met_py, 0.0, *pf_met_pt);

  // create and fill Jet vector
  pfjets = new std::vector<mut::Jet>;
  for (int i=0;i < n_pfjet;i++) {
    if (**pfjet_energy[i] > 0) {
      pfjets->emplace_back(**pfjet_pt[i], **pfjet_eta[i], **pfjet_phi[i], **pfjet_energy[i]);
      pfjets->back().setPartonFlavour(**jet_flavour[i]);
      std::vector<std::pair<std::string, float>> disPairs;
      for  (auto const &a_disc : pfjet_disc.at(i)) {
        disPairs.emplace_back(a_disc.first,**a_disc.second);
      }
      pfjets->back().setDiscriminatorPairs(disPairs);
    }
  }

    // create and fill Muon vector
    muons = new std::vector<mut::Lepton>;
    for (int i=0;i < n_muon;i++) {
    if (**muon_energy[i] > 0) {
       muons->emplace_back(**muon_pt[i], **muon_eta[i], **muon_phi[i], **muon_energy[i]);
    } else {
      return false;
    }
    // add isolation variables
    std::vector<std::pair<std::string, float>> isoPairs;
    isoPairs.emplace_back("relIso", **muon_relIso[i]);
    muons->back().setLeptonIsoPairs(isoPairs);
  }

  ttree->Fill();

  delete eventInfo;
  delete pfjets;
  delete pfmet;
  delete muons;

  return true;
}

// all entries have been processed (executed in slave)
void ConverterRunOne::SlaveTerminate()
{

}

// last function called (on client)
void ConverterRunOne::Terminate()
{
  TTree* ttree = dynamic_cast<TTree *>(fOutput->FindObject(Form("tree"))); 

  TFile *o_file = new TFile(o_filename.c_str(), "RECREATE");
  if ( o_file->IsOpen() ) std::cout << "File is opened successfully" << std::endl;
  ttree->Write();
  fOutput->Clear(); 
}
