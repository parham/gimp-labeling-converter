<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/TORNGATS/batman-ebt">
    <img src="https://www4.fsa.ulaval.ca/wp-content/uploads/2018/12/fsaulaval.jpg" alt="Logo" width="320" height="100">
  </a>
  <a href="https://github.com/TORNGATS/batman-ebt">
    <img src="https://torngats.ca/css/img/logo-en_US.png?1603473813" alt="Logo" width="320" height="100">
  </a>

  <h3 align="center">GIMP Labeling Assistance</h3>
  <h4 align="center">Converting images labeled by GIMP to different formats</h4>

  <br/>
  <br/>

  </p>
</p>


#### GNU Image Manipulation Program
GIMP (GNU Image Manipulation Program) is a free and open-source raster graphics editor used for image manipulation (retouching) and image editing, free-form drawing, transcoding between different image file formats, and more specialized tasks. It is not designed to be used for drawing. 

#### Labeling Procedure
GIMP is a powerful photo editing software which has great potential to be used as a labeling software for _semantic segmentation_. To do so, we provide a procedure for labeling images using GIMP software,
- Load an image into the software.
- Review the image to find candidate classes.
- Create a layer for each class (make sure that the background is transparent)
- Use pen tool and select a color (make sure the "hardness" and "opacity" properties are set to 100.
- Draw the areas belong to the class associated to the selected layer.
- Change the layer and repeat the labeling steps.
- Save the image as "xcf" file format.

<p align="center">
  <img src="resources/gimp_labeling.png" width="900" title="Software screenshot">
</p>

#### Program
This repository provides a CLI tool that converts XCF file to a new format suitable for labeling. The tool also make the users able to add their own handlers for addling support to other types of outputs. Currently, the tool supports two handlers,
- _mask_ : convert the xcf files to a multiple folders named after extracted classes. Each folder contains the mask presenting the areas labeled as the associated class.
- _coco_ : convert the xcf files to a single MS COCO file (JSON).
- _class_map_ : convert the xcf files to images that each pixel labeled as its class index.

The cli tool can be initialized in two ways: (a) using config files, and (b) using commandline arguments.

##### Options

The CLI tool provides the following options,

| **Options**  	| **Other forms** 	| **Description**                            	              |
|--------------	|-----------------	|-----------------------------------------------------------|
| --dir_in     	| --dir -d        	| Directory containing the images.                        	|
| --file_out   	| --out -o        	| Output Directory                           	              |
| --handler    	| --type          	| Handler Type [initially "mask", "class_map" and "coco"] 	|
| --num_worker 	| -w              	| Number of Workers                                       	|
| --config     	|                 	| Configuration file path                                 	|
| --name       	| -n              	| Set dataset name                                        	|
| --info       	|                 	| Set description                                         	|
| --url        	|                 	| Set URL                                                 	|
| --version    	|                 	| Set version                                             	|
| --year       	|                 	| Set Year                                                 	|
| --contrib    	|                 	| Set contributor                                         	|
| --category   	| -c              	| Class Categories                                         	|

#### Installation

```
pip install cython
pip install git+https://github.com/waspinator/coco.git@2.1.0
pip install git+https://github.com/waspinator/pycococreator.git@0.2.0

pip install gimp-labeling-converter

```


#### Usage

##### Using options

```
gimp_labeling_converter --dir "/home/phm/my-dataset/labeled" \
                --out "/home/phm/Documents/dataset" \
                --type "mask" -w 5 \
                -c "defect" -c "surface_defect" \
                -n "Parham Test"
```

or 

```
gimp_labeling_converter --dir "/home/phm/my-dataset/labeled" \
                --out "/home/phm/Documents/dataset/test.json" \
                --type "coco" -w 5 \
                -c "defect" -c "surface_defect" \
                -n "Parham Test" --info "Testing the coco handler" \
                --url "linkedlist.com" \
                --version "1.0.0" --year 2022 --contrib "Parham Nooralishahi"
```

##### Using config file

Assuming the config file named as "./coco.json",

```
gimp_labeling_converter --config "./coco.json"
```

##### JSON Configuration file samples

For mask handler:
```
{
    "dir_in" : "/home/phm/datasets/Pipe_Inspection/pipe_inspection_group01_20201117/label_orig",
    "file_out" : "/home/phm/Documents/temp", 
    "handler" : "mask",
    "category" : {
        "defect" : 1, 
        "surface_defect" : 2
    },
    "num_workers" : 10
}
```

For coco handler:
```
{
    "dir_in" : "/home/phm/GoogleDrive/Personal/Datasets/my-dataset/thermal-segmentor/Pipe_Inspection/pipe_inspection_group01_20201117/label_orig",
    "file_out" : "/home/phm/Documents/temp/phm.coco", 
    "handler" : "coco",
    "num_workers" : 10,
    "category" : {
        "defect" : 1, 
        "surface_defect" : 2
    },
    "dataset_name" : "Pipe_Inspection",
    "description" : "Test COCO",
    "url" : "phm.com",
    "version" : "1.0.0",
    "year" : 2022,
    "contributor" : "Parham Nooralishahi"
}
```


## XCF Dataset

Another feature provided in this repository is the customized dataset for Pytorch designed to handle XCF dataset.

## Contact
Parham Nooralishahi - parham.nooralishahi@gmail.com | [@phm](https://www.linkedin.com/in/parham-nooralishahi/) <br/>

