![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

############################################################
---------------------------------------------------------


We explored YOLO/DarkNet for identifying and localising malignant tumours from breast mammograms, using the original DDSM dataset. In this README, we will cover some tips + tricks that we picked up along the way!

Tutorials
---

There a number of really good tutorials on training DarkNet from scratch, including labelling data in the correct format and parametr tuning considersations. These tutorials are what we used to get started, and are listed below. 

https://pjreddie.com/darknet/
https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/


Install DarkNet
---------------

This is well-explained by pjreddie in the README of the original repo. Find instructions at:

https://pjreddie.com/darknet/install/

We cloned and 'built' DarkNet, in July 2017.

NOTE: If using a GPU, remember to change the first line of the Makefile in the base directory to read: GPU=1  


Data prep
---------

We used the raw unprocessed DDSM dataset. This is accessible on the GliaLab S3 bucket: 'fulldataset/imagesOnePlay/cancers/'

The following scripts may be useful for you:

*rewritecsv.py* - Reads file names and bounding box coordinates, converts them to YOLO format and writes them back to a file. Assumes the original files has the format: TO COME

*transfer_files.py* - Transfer jpeg files to a different folder


TRAIN-TEST split
----------------

We must explicitly define train.txt and test.txt files with the names of train/test data. This is discussed in tutorials above. We used the following script after first converting data to YOLO bounding box format.

*data_split.py* - Split data into train and test sets, and write to corresponding text files


TRAINING
----------------

See tutorials! 

EVALUATING
----------------

Once we have the trained model weights, we can predicting bounding boxes for our test setusing saved weights:

`./darknet detector valid cfg/obj.data cfg/yolo-obj.cfg backup/run_1_cancers_only/yolo-obj_10000.weights`

This outputs bounding box co-ordinates into a text file (named by default as 'comp4_det_test_cancer.txt' _but this can be changed) stored under 'results'. Remember to update the .data, .cfg and .weights files to your saved files!

Using this output, we can then evaluate the model using Intersection over Union (IOU). Good explanation here - http://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/

A Jupyter notebook showing this calculation is also included.

RESULTS
---------

We evaluated the results on a hold-out set by computing 'intersection over union' (IOU); a script for generating this is included.

IOU results for network trained with input images being re-sized to 416x416, but tested at different scales:

*test image input size: 416,416*    

| **mean**|  0.049828  |  
| **std** |  0.141468  |   
| **min** |  0.000000  |  
| **max** |  0.887157  |  

*test image input size: 832,832  -  UPDATE!*
| **mean**|  0.049828  |  
| **std** |  0.141468  |   
| **min** |  0.000000  |  
| **max** |  0.887157  | 

*test image input size: 1244,1244 *
| **mean**|  0.043643  |  
| **std** |  0.153892  |   
| **min** |  0.000000  |  
| **max** |  0.999996  | 
  
Useful commands
---------------

Transferring files from EC2 instance to local machine (works in the opposite direction too, by switching source and target):  

`scp -i ec2key.pem username@ec2ip:/path/to/file ./target_dir/`

GNU screen:  


Useful links + tutorials
-------------------------

Google threads for YOLO/DarkNet: https://groups.google.com/forum/#!searchin/darknet/get$20bounding$20box%7Csort:relevance/darknet/au4B7aTSofE/jWktLKhmEQAJ

YOLO TensorFlow implementation: 
https://github.com/johnwlambert/YoloTensorFlow229


authors: 
---------
Belal C
Sailesh B
