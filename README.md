
# LJMET_converter

A selector to convert LJMET ROOT TTrees (both from
Run I and Run II) to [mut_dataformat](https://github.com/pablodecm/mut_dataformats)
ROOT TTrees.

## Installation

* setup your CMSSSW area (use modern version please)

```
    export SCRAM_ARCH=slc6_amd64_gcc491
    cmsrel CMSSW_7_4_14
    cd CMSSW_7_4_14/src/
    cmsenv
```

* clone mut_dataformats and LJMET_converter repositories  

```
    git clone https://github.com/pablodecm/mut_dataformats.git mut_framework/mut_dataformats
    git clone https://github.com/pablodecm/LJMET_converter.git mut_framework/LJMET_converter
```

* compile everything with SCRAM

```
    scram b -j 8
```

## Usage

For Run II 25ns data and MC samples, the
ConverterRunTwo_25ns.py can be used to
process any specific sample in
[python/samples_25ns.py](https://github.com/pablodecm/LJMET_converter/blob/master/python/samples_25ns.py) or all of them.

Use the --input_folder and --output_folder
parameters to specify the location of your
LJMET directory and where do you want to save
the converted ROOT TTrees. 

