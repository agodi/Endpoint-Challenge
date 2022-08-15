<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project emulates a file manager, the python script can perform four basic operations:

* Create a directory
* Move a directory to another directory
* Delete a directory
* List all directories

All operations are executed starting at the base directory or "home" which doesn't have a name.

The sequence of operations to perform are read from an input file. Operations are defined using the following format:
* LIST
* CREATE \<directory to create>
* MOVE \<directory to move> \<destination directory>
* DELETE \<directory to remove>

CREATE, MOVE and DELETE operations require the full path to the directories.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

### Prerequisites

To run the script Python 3 must be installed.
* Visit https://www.python.org/downloads to download Python 3.7 or later 


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/agodi/Endpoint-Challenge.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

To run the script open a terminal, go to the directory where this repo was cloned and enter the following command:
   ```sh
   python challenge.py <input-file>
   ```
Replace \<input-file> with the full path to the file you desire to use as input. If no path is provided the script will try to use the default file included in this repo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Arturo Gomez - agomdia@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/agodi
