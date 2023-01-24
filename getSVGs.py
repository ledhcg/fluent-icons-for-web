from bs4 import *
import requests
import os

# CREATE FOLDER


def folder_create(images):
    try:
        folder_name = input("Enter Folder Name:- ")
        # folder creation
        os.mkdir(folder_name)

    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        folder_create()

    # image downloading start
    download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):

    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

            # 1.data-srcset
            # 2.data-src
            # 3.data-fallback-src
            # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # Format link: https://github.com/microsoft/fluentui-system-icons/raw/master/assets/Access%20Time/SVG/ic_fluent_access_time_24_filled.svg?raw=true
            image_link = 'https://github.com/' + image_link.replace(" ", "%20")

            # After getting Image Source URL
            # We will try to get the content of image
            downloadSVG(image_link, folder_name)
            count += 1
            # try:
            #     r = requests.get(image_link).content
            #     try:

            #         # possibility of decode
            #         r = str(r, 'utf-8')

            #     except UnicodeDecodeError:

            #         # After checking above condition, Image Download start
            #         with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
            #             f.write(r)

            #         # counting number of image downloaded
            #         count += 1
            # except:
            #     pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

# DOWNLOAD IMAGE SVG


def downloadSVG(img, folder_name):

    # Format file from "https://github.com/microsoft/fluentui-system-icons/raw/master/assets/Access%20Time/SVG/ic_fluent_access_time_24_filled.svg?raw=true" to "ic_fluent_access_time_24_filled.svg"
    file_name = img.split('/')[-1][:-9]

    # Format name from "ic_fluent_access_time_24_filled.svg" to "access-time-24-filled"
    image_name = file_name[:-4][10:].replace("_", "-")
    type_file = file_name.split('.')[-1]
    if type_file == "svg":
        print(f"Type file: {type_file} | Image name: {image_name}")
        # Now let's send a request to the image URL:
        r = requests.get(img, stream=True)
        # We can check that the status code is 200 before doing anything else:
        if r.status_code == 200:
            # This command below will allow us to write the data to a file as binary:
            with open(f"{folder_name}/{image_name}.svg", "wb+") as f:
                for chunk in r:
                    f.write(chunk)
        else:
            # We will write all of the images back to the broken_images list:
            broken_images.append(img)


# MAIN FUNCTION START
def main(url):

    # content of URL
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    folder_create(images)


# take url
url = input("Enter URL:- ")

# CALL MAIN FUNCTION
main(url)

# Run file
# python getFlags
# url: https://github.com/microsoft/fluentui-system-icons/blob/master/icons_filled.md
# folder: assets
# https://iconduck.com/sets/fluent-ui-system-icons
