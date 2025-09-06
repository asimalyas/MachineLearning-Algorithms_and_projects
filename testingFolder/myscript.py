from icrawler.builtin import GoogleImageCrawler
import os

# List of names (with spaces, icrawler handles them)
names = ["Allama Iqbal", "Quaid Azam"]

# Number of images per person
num_images =40

# Folder to save images
base_dir = "downloaded_images"

# Make base folder if it doesn't exist
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for name in names:
    print(f"Downloading images for {name}...")
    
    # Create folder for each person
    person_dir = os.path.join(base_dir, name.replace(" ", "_"))
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
    
    crawler = GoogleImageCrawler(storage={"root_dir": person_dir})
    crawler.crawl(keyword=name, max_num=num_images)
    
    print(f"Done: {name}\n")
