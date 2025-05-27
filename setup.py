from setuptools import setup, find_packages
import logging

# Load requirements from file
def load_requirements(filename):
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except FileNotFoundError:
        logging.warning("requirements.txt not found. Proceeding without it.")
        return []

install_reqs = load_requirements("requirements.txt")

setup(
    name='mask-rcnn',
    version='2.1',
    url='https://github.com/matterport/Mask_RCNN',
    author='Matterport',
    author_email='waleed.abdulla@gmail.com',
    license='MIT',
    description='Mask R-CNN for object detection and instance segmentation',
    packages=find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.6',
    long_description="""This is an implementation of Mask R-CNN on Python 3, Keras, and TensorFlow. 
The model generates bounding boxes and segmentation masks for each instance of an object in the image. 
It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.""",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Image Segmentation",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords="image instance segmentation object detection mask rcnn r-cnn tensorflow keras",
)
