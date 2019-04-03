# goal programming 

programming = optimization 

## apa itu 
Goal programming is a way to satisfy (sometimes conflicting) goals by ranking the goals by priority. The optimization algorithm will attempt to optimize each goal one at a time, starting with the goal with the highest priority and moving down through the list. Even if a goal cannot be satisfied, the goal programming algorithm will move on when it has found the best possible answer. Goals can be roughly divided into two types:

As long as we satisfy the goal, we do not care by how much. If we cannot satisfy a goal, any lower priority goals are not allowed to increase the amount by which we exceed (which is equivalent to not allowing any change at all to the exceedance).
We try to achieve as low a value as possible. Any lower priority goals are not allowed to result in an increase of this value (which is equivalent to not allowing any change at all).
In this example, we will be specifying two goals, on for each type. The higher priority goal will be to maintain the water level of the storage element between two levels. The lower priority goal will be to minimize the total volume pumped.

- solving the infeasible solution from LP model

>Charnes and Cooper (1961, p. 215) put it this way:
"Whether goals or attainable or not, an objective may then be stated in which
optimization gives a result which comes 'as close as possible' to the indicated
goals." 

## research paper menarik

## implementasi goal programming 
- two version of GP (Chanes and Cooper, 1961)
  - weighted (punya prioritas)
    - min: $Z = \sum_{i \in m} P_i * \sum_{k=1}^{n_i}(w_{ik}^+ d_i^+ + w_{ik}^- d_i^-)$
    - subject to: $\sum_{j=1}^na_{i,j}x_j-d_i^+ + d_i^- = b_i$
    - dimana $P_i > P_{i+q} > P_{i+2}$ (prioritas soft criteria ke-i)
  - lexicographic (seperate priorities)
    - min: $Z = \sum_{i\in m} P_i (d_i^+ + d_i^-)$
    - s.t.: $\sum_{j=1}^n a_{ij} x_{j} - d_i^+ + d_i^- = b_i$
- biasa diguanakn di ms/or (management science / operation research)
  - multiple criteria decision making (mcdm)
  - solving managerial problems when multiple objectives are present
  ![](img/bagian_GP_pada_MSOR.png)
--------


## bikin ppt 

------
# references

## contoh soal cantik 
[multivariable optimization pake prioritas](http://prejudice.tripod.com/ME30B/two_gp.htm)
## contoh soal pake solver (Excel)
https://www.youtube.com/watch?v=Ytzr3LY6iS0
https://www.youtube.com/watch?v=iIdDPl2nkYo

## references
- [optimization with python](https://www2.hawaii.edu/~jonghyun/classes/S18/CEE696/schedule.html)
    - only needed [this](https://www2.hawaii.edu/~jonghyun/classes/S18/CEE696/files/04_scipy_optimize.pdf)
    - and [this](https://www2.hawaii.edu/~jonghyun/classes/S18/CEE696/files/08_scipy_optimize2.pdf)


