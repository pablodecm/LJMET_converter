#define ConverterRunTwo_cxx
#include "../interface/ConverterRunTwo.h"

// start of query (executed on client)
void ConverterRunTwo::Begin(TTree * /*tree*/)
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
void ConverterRunTwo::SlaveBegin(TTree * /*tree*/)
{

   TString option = GetOption();

  ttree = new TTree("tree","Physics Object based TTree");

  ttree->Branch("eventInfo","mut::EventInfo", &eventInfo, 64000,1);
  ttree->Branch("pfmet","mut::MET", &pfmet, 64000,1);
  ttree->Branch("pfjets","std::vector<mut::Jet>", &pfjets, 64000,1);
  ttree->Branch("muons","std::vector<mut::Lepton>", &muons, 64000,1);

  fOutput->Add(ttree);  

  
  disc_names.emplace_back("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
  disc_names.emplace_back("pfCombinedMVABJetTags");

 for ( std::string disc_name : disc_names ) { 
    std::string b_name = disc_name+"_BTagSFCalc";
    pfjet_disc.emplace_back(disc_name, std::unique_ptr<TTreeReaderValue<std::vector<double>>>(new TTreeReaderValue<std::vector<double>>(reader,b_name.c_str())));
  }

}

// for each entry of the TTree
Bool_t ConverterRunTwo::Process(Long64_t entry)
{

  // set TTreeReader entry
  reader.SetEntry(entry);

  // create and fill EventInfo
  eventInfo = new mut::EventInfo(int(*event), *lumi, *run);
  eventInfo->setNumPV(*nPV);
  std::vector<std::pair<std::string, bool>> filterPairs;
  eventInfo->setFilterPairs(filterPairs);
  std::vector<std::pair<std::string, float>> weightPairs;
  eventInfo->setWeightPairs(weightPairs);

  // create and fill mut MET
  pfmet = new mut::MET();
  pfmet->SetPxPyPzE((*pf_met_energy)*std::cos(*pf_met_phi),
                    (*pf_met_energy)*std::sin(*pf_met_phi),
                    0.0, *pf_met_energy);

  // create and fill Jet vector
  pfjets = new std::vector<mut::Jet>;
  for (std::size_t i=0;i < pfjet_energy->size(); i++) {
    pfjets->emplace_back(pfjet_pt->at(i), pfjet_eta->at(i),
                         pfjet_phi->at(i), pfjet_energy->at(i));
    pfjets->back().setPartonFlavour(jet_flavour->at(i));
    std::vector<std::pair<std::string, float>> disPairs;
    std::cout << "energy size" << pfjet_energy->size() << std::endl;
    for  (auto const &a_disc : pfjet_disc) {
      disPairs.emplace_back(a_disc.first,(**a_disc.second).at(i));
      std::cout << "disc size" << (**a_disc.second).size() << std::endl;
      pfjets->back().setDiscriminatorPairs(disPairs);
    }
  }

  // create and fill Muon vector
  muons = new std::vector<mut::Lepton>;
  for (std::size_t i=0;i < muon_energy->size();i++) {
    muons->emplace_back(muon_pt->at(i), muon_eta->at(i), muon_phi->at(i), muon_energy->at(i));
    // add isolation variables
    std::vector<std::pair<std::string, float>> isoPairs;
    std::cout << "relIso" << muon_relIso->size() << std::endl;
    std::cout << "energy" << muon_energy->size() << std::endl;
    isoPairs.emplace_back("relIso", muon_relIso->at(i));
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
void ConverterRunTwo::SlaveTerminate()
{

}

// last function called (on client)
void ConverterRunTwo::Terminate()
{
  TTree* ttree = dynamic_cast<TTree *>(fOutput->FindObject(Form("tree"))); 

  TFile *o_file = new TFile(o_filename.c_str(), "RECREATE");
  if ( o_file->IsOpen() ) std::cout << "File is opened successfully" << std::endl;
  ttree->Write();
  fOutput->Clear(); 
}
