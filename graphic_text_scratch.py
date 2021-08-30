from image_processing_functions import *

input_directory = 'C:/Users/Vvayne/'
runs = 50

now = datetime.datetime.now()

output = 'C:/Users/Vvayne/Documents/FA 2018/General/Outputs/' + now.strftime("%Y-%m-%d")
if not os.path.exists(output):
    os.makedirs(path=output)
os.chdir(output)

for i in range(runs):

    create_cubomanic(input_directory,output,columns=0,rows=0,conversions=True)
    merge_random_images(input_directory,output,size=(2700,3600))
    if isinstance(output, str):
        # print(output)
        output = output.split(" C")

    # print(output)
    # print(final_directory)
    # print(final_directory.type)
    # print("makin a cubomanic")
    # create_cubomanic([output_directory,text_image_pages,final_directory],output_directory,columns=900,rows=1200,conversions=True)
    # print("now let's make a stripomanic")

    d1 = input_directory

    image1 = None
    image2 = None
    fail_count = 0
    while not image1 or not image2:
        try:
            image1 = sample(get_imlist(directory=d1), 1)[0]
            # print(image1)
            image2 = sample(get_imlist(directory=final_directory), 1)[0]
            # print(image2)
        except:
            print('keep looking for images')
            fail_count += 1
            if fail_count >= 20:
                break
    if image1 and image2:
        print('got images to blend')
        create_stripomanic([text_image_pages], d1, columns=900, rows=1200, orientation='horizontal')
        merge_images(image_path1=image1, image_path2=image2, size=(900, 1200), save_directory=final_directory)