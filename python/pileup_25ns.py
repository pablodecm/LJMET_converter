

pu_dists = {}

# ideal MC PU distribution for 25 ns samples
# from https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/SimGeneral/MixingModule/python/mix_2015_25ns_Startup_PoissonOOTPU_cfi.py
pu_dists["winter15_MC"] = [
                           4.8551e-07,
                           1.74806e-06,
                           3.30868e-06,
                           1.62972e-05,
                           4.95667e-05,
                           0.000606966,
                           0.003307249,
                           0.010340741,
                           0.022852296,
                           0.041948781,
                           0.058609363,
                           0.067475755,
                           0.072817826,
                           0.075931405,
                           0.076782504,
                           0.076202319,
                           0.074502547,
                           0.072355135,
                           0.069642102,
                           0.064920999,
                           0.05725576,
                           0.047289348,
                           0.036528446,
                           0.026376131,
                           0.017806872,
                           0.011249422,
                           0.006643385,
                           0.003662904,
                           0.001899681,
                           0.00095614,
                           0.00050028,
                           0.000297353,
                           0.000208717,
                           0.000165856,
                           0.000139974,
                           0.000120481,
                           0.000103826,
                           8.88868e-05,
                           7.53323e-05,
                           6.30863e-05,
                           5.21356e-05,
                           4.24754e-05,
                           3.40876e-05,
                           2.69282e-05,
                           2.09267e-05,
                           1.5989e-05,
                           4.8551e-06,
                           2.42755e-06,
                           4.8551e-07,
                           2.42755e-07,
                           1.21378e-07,
                           4.8551e-08
                          ]

# PU estimated from data (with pileupCalc.py)                          
# data JSON file used was Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt

# best min xs fit
pu_dists["data_69000mb"] = [
                            4.7027036340041865e-05,
                            0.00028156458062175845,
                            0.00028436970428522836,
                            0.00038726956061482223,
                            0.0005694213265605517,
                            0.0009521227914286149,
                            0.0031906887830406294,
                            0.020318240952431184,
                            0.0699736080060523,
                            0.13006763694560458,
                            0.18007697940970965,
                            0.19887586471512797,
                            0.17400645729117695,
                            0.11877177747003019,
                            0.06317000671388909,
                            0.026530990255221584,
                            0.009020682240901506,
                            0.0025800600738514457,
                            0.0006598826626958958,
                            0.00016491901890610568,
                            4.466055279790666e-05,
                            1.4445130053557087e-05,
                            5.837907113017267e-06,
                            2.780256010831433e-06,
                            1.4051658722144094e-06,
                            7.022498895828814e-07,
                            3.3667879872641223e-07,
                            1.532943541487815e-07,
                            6.609970531985645e-08,
                            2.6973544388051847e-08,
                            1.041540333496139e-08,
                            3.805388191826317e-09,
                            1.315533577280956e-09,
                            4.30311082571365e-10,
                            1.331800565457274e-10,
                            3.900058374876329e-11,
                            1.0806328017980027e-11,
                            2.833093182989862e-12,
                            7.027816855903317e-13,
                            1.649524094740059e-13,
                            3.663345438260294e-14,
                            7.698056091350712e-15,
                            1.5306351266278717e-15,
                            2.879722568244442e-16,
                            5.126726575168171e-17,
                            8.63512643268303e-18,
                            1.3768786700867553e-18,
                            2.0428597310075792e-19,
                            3.724847746220679e-20,
                            3.724847746220679e-20,
                            3.724847746220679e-20,
                            3.724847746220679e-20,
                            3.724847746220679e-20
                            ]

       
# best min xs fit +5%
pu_dists["data_72450mb"] = [
                            4.029516085464934e-05,
                            0.0002544965838377415,
                            0.0002809891094592884,
                            0.0003357167553704894,
                            0.0005083900175247793,
                            0.0007464259720239938,
                            0.0018615256216538891,
                            0.010080360534509817,
                            0.04451139705959828,
                            0.09823191506013326,
                            0.1501427336670173,
                            0.18458543583799764,
                            0.18490471484018559,
                            0.14891125165862779,
                            0.09547749098448052,
                            0.04891794919401964,
                            0.020323997521971875,
                            0.007013882880322576,
                            0.0020848194373633785,
                            0.0005648340817644684,
                            0.00015094755977342026,
                            4.352276764735437e-05,
                            1.4730188480303584e-05,
                            6.107803276158779e-06,
                            2.9697141423918438e-06,
                            1.545167545253454e-06,
                            8.032857409869741e-07,
                            4.039183439609345e-07,
                            1.9412673304723753e-07,
                            8.884857139960349e-08,
                            3.868633837911351e-08,
                            1.6021465906321572e-08,
                            6.310445543964579e-09,
                            2.3638740678779403e-09,
                            8.421556813866951e-10,
                            2.8533987921028855e-10,
                            9.194615679094026e-11,
                            2.817768270417978e-11,
                            8.212543693647938e-12,
                            2.276415464918614e-12,
                            6.001060301164234e-13,
                            1.504557509751552e-13,
                            3.587534557006917e-14,
                            8.135654710524467e-15,
                            1.7546938810361909e-15,
                            3.5993604727775595e-16,
                            7.02214588091765e-17,
                            1.3027817995449802e-17,
                            2.2986439108366076e-18,
                            3.875143598831092e-19,
                            7.223592329084711e-20,
                            7.828049027103546e-22,
                            7.828049027103546e-22
                           ]

# best min xs fit -5%
pu_dists["data_65550mb"] = [
                           5.482342935603643e-05,
                           0.0003110101233555503,
                           0.0002943819714977439,
                           0.000447642258484305,
                           0.000648535385624581,
                           0.0013087172199099523,
                           0.006426265205947095,
                           0.038672555763296944,
                           0.10215477275939988,
                           0.1657717129890969,
                           0.20568202570554064,
                           0.1985706527234064,
                           0.14652083843716815,
                           0.08194335220364395,
                           0.0350991794478901,
                           0.011809512017409082,
                           0.003250420476445059,
                           0.0007816942366439545,
                           0.00018147718437413882,
                           4.584992574817515e-05,
                           1.4118362566043573e-05,
                           5.552929562860932e-06,
                           2.5823280333289713e-06,
                           1.2608768821544131e-06,
                           6.017594257925806e-07,
                           2.7307917141651476e-07,
                           1.1686686309663515e-07,
                           4.7069111799832475e-08,
                           1.7833152128371973e-08,
                           6.355190354955844e-09,
                           2.130237496277023e-09,
                           6.716185415671081e-10,
                           1.9916370413167085e-10,
                           5.5550655428982536e-11,
                           1.4573340909583693e-11,
                           3.596005122618115e-12,
                           8.345912063257807e-13,
                           1.8218870508968806e-13,
                           3.740810925957927e-14,
                           7.224534286450726e-15,
                           1.3123735993039306e-15,
                           2.242410268285977e-16,
                           3.603833480530987e-17,
                           5.449061171180061e-18,
                           7.766048242138447e-19,
                           1.0402120225803184e-19,
                           1.246854563251748e-20,
                           1.246854563251748e-20,
                           1.246854563251748e-20,
                           1.246854563251748e-20,
                           1.246854563251748e-20,
                           1.246854563251748e-20,
                           1.246854563251748e-20
                          ]
