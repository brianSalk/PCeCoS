# PCeCoS

**P**rimitive **Ce**lls **Co**lony **S**imulation - 
very simple simulator of cells colony growth on square nutrient medium.

+ **Nutrient matrix** with constant shape
  + Color
    + black - _resource = 1_
    + grey - resource = (0, 1)
    + white - resource = 0
  + Matrix is being resupplied with constant rate
+ Every **cell colony** started from 1 cell.
  + number of colonies is specified (<font color=red>No more than 6 colonies are currently available</font>)
  + cells consume resources nearby (within a 3 x 3 submatrix) from the maximum 
resource level _box_ with a certain frequency specific to each cell colony 
  + cells divides when reach "**division resource level**"
  + they divide in the direction of maximum resource level nearby (3 x 3 submatrix)
  + if there are not enough resources nearby, the cell dies.
+ **Animation** are saved as _.gif_ file
  + Number of rounds (frames) is specified

> **NB!** Tool is not parallelized! All calculations are performed sequentially. 
> Thus, the larger the number of colonies and the size of the matrix, 
> the longer it takes to complete the animation.

## Install

``` bash
git clone https://github.com/vladissta/PCeCoS
cd PCeCoS
```
#### Virtual environment setting

``` bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
usage: process.py [-h] [-c [COLONY_NUMBER]] [-m MATRIX_SHAPE MATRIX_SHAPE] [-f [FRAMES]] [-r [RESUPPLY_RATE]] [-d [DIVISION_LEVEL]] [--output [OUTPUT]]

Primitive Cell Colony Simulator

options:
  -h, --help            show this help message and exit
  -c [COLONY_NUMBER], --colony-number [COLONY_NUMBER]
                        Number of colonies (default: 2)
  -m MATRIX_SHAPE MATRIX_SHAPE, --matrix-shape MATRIX_SHAPE MATRIX_SHAPE
                        Matrix shape (default: 30 30)
  -f [FRAMES], --frames [FRAMES]
                        Number of rounds (frames) (default: 30)
  -r [RESUPPLY_RATE], --resupply-rate [RESUPPLY_RATE]
                        Resupply rate of resource (default: 0.05)
  -d [DIVISION_LEVEL], --division-level [DIVISION_LEVEL]
                        Division resource level (default: 1)
  --output [OUTPUT]     Output filename (default: animation.gif)

```

## Example of result visualization

![](animations/animation.gif)

### Parameters
> **COLONIES_NUMBER** = 5  
**MATRIX_SHAPE** = 100, 100  
**DIVISION_RESOURCE_LEVEL** = 1  
**ROUNDS_NUMBER** = 60  
**RESUPPLY_RATE** = 0.05  
