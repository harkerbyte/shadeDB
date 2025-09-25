from setuptools import setup, find_packages

setup(
    name="shadeDB",
    version="0.1.3",
    description="A class oriented lightweight database with a cli wrapper for any device: store, update, copy, and remove structured data with a single command. Perfect for embedded devices, mobiles, devtools, and quick local services.",
    author="Shade",
    author_email="adesolasherifdeen3@gmail.com",
    entry_points={
        "console_scripts": [
          "shadecrypt=shadecrypt.cli:main",
          "scdb=shadecrypt.cli:main"
        ]
    },
    include_package_data=True,
    python_requires='>=3.8',
    license="GPL-3.0",
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Environment :: Console",
      "Intended Audience :: Developers",
      "Topic :: Database :: Database Engines/Servers",
    ],
    project_urls={
        "GitHub": "https://github.com/harkerbyte",
        "Facebook": "https://facebook.com/harkerbyte",
        "Whatsapp" : "https://whatsapp.com/channel/0029Vb5f98Z90x2p6S1rhT0S",
        "Youtube" : "https://youtube.com/@harkerbyte",
        "Instagram": "https://instagram.com/harkerbyte"
    },
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)