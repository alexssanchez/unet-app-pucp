import numpy, shutil, os, nibabel
import imageio
import sys, getopt

def convert(inputfile, outputfile):
    
    # set fn as your 4d nifti file
    image_array = nibabel.load(inputfile).get_data()
    #print(len(image_array.shape))
    # else if 3D image inputted
    if len(image_array.shape) == 3:
        # set destination folder
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)
            #print("Created ouput directory: " + outputfile)
        #print('Reading NIfTI file...')
        total_slices = image_array.shape[2]
        slice_counter = 0
        # iterate through slices
        for current_slice in range(0, total_slices):
            # alternate slices
            if (slice_counter % 1) == 0:
                # rotate or no rotate
                data = image_array[:, :, current_slice]
                #alternate slices and save as png
                if (slice_counter % 1) == 0:
                    #print('Saving image...')
                    image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    imageio.imwrite(image_name, data)
                    #print('Saved.')
                    #move images to folder
                    #print('Moving image...')
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1
                    #print('Moved.')
        #print('Finished converting images')
    else:
        print('Not a 3D or 4D Image. Please try again.')