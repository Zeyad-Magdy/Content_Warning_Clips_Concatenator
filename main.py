import os
from moviepy.editor import concatenate_videoclips, VideoFileClip
from datetime import datetime
import tempfile


def combine_webm_files():
    
    # Get the path to the temporary folder
    temp_folder = tempfile.gettempdir()
    main_directory = os.path.join(temp_folder, 'rec')
    # Iterate over all folders in the specified directory
    for index,directory in enumerate(os.listdir(main_directory)):
        directory_path = os.path.join(main_directory, directory)
        print(directory,directory_path)
        if os.path.isdir(directory_path):
            print(f"Processing directory {index + 1}: {directory_path}")
            # Get a list of all directories in the specified directory
            directories = [os.path.join(directory_path, folder) for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
            found_count = 0 # Initialize a counter for found .webm files
            # List to hold all video clips
            clips = []
            # print(directories)
            # Sort directories by last modification time
            directories.sort(key=lambda x: os.path.getmtime(x))
            for folder_path in directories:
                
                # Check if output.webm exists in the folder
                webm_file = os.path.join(folder_path, 'output.webm')
                if os.path.exists(webm_file):
                    # Increment the found count
                    found_count += 1
                    # Print the updated count on the same line
                    print(f"\rFound {found_count}", end="")
                    # Add the video clip to the list
                    clips.append(VideoFileClip(webm_file))

            if not clips:
                print("\nNo .webm files found in the specified directory.")
                return
            print("\nprocessing...")
            # Concatenate all clips into a single clip
            final_clip = concatenate_videoclips(clips)
            # Write the final clip to a file
            #make name of file : output_datetime.webm
            now = datetime.now()
            output_file = "output_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".webm"
            final_clip.write_videofile(output_file, codec='libvpx')
        print("Processing complete for directory:", directory_path)


def main():
    # Ask for the directory containing the folders
    # directory = input("Please enter the directory containing the folders (or 'q' to quit): ")
    

    # Process the directory
    combine_webm_files()


    

if __name__ == "__main__":
    main()