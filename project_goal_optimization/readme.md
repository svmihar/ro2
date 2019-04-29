# goal programming 
multiple criteria decision-making (MCDM/A)

## tools
- python 
  - pyomo (making the mathematical to pythonic code)
  - LP solver:
    - [GNU Linear Programming Kit](https://www.gnu.org/software/glpk/) 
      - used when feasible solution is available
    - [CBC](https://projects.coin-or.org/Cbc)
      - used to detect infeasible solution

## skripsi simulation 
[model goal programming untuk optimasi produkaksesoris]()
discussed topics
- modelling the problem 
- solving with weighted GP 
- using primal-dual Linear Programming for feasible solutions

problems: 
- can't use chebyshev, classical nor lexicographical due to bounds problems (primal-dual)
- no feasible solutions from pyomo


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
[Go to Research Paper Directory](https://github.com/atriple/ro2/tree/master/project_goal_optimization/research_paper)

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

  ### Practical Goal Programming (Dylan jones, Mehrdad Tamiz, 2010)
  - Jenis
    - Generic
    - Distance Based
      - **Lexicographic**
        - *priorities goals over others.*
        - has a number of priority levels
        - predefined set of goals 
        - no direct 'trade off' comparisons between goals. 
        - contoh?
      - **Weighted** 
        - chooses set of decision variable values which together *make the achievement function lowest*. 
          - makes other goals have a poor result  
        - allow directr trade off between unwanted deviational variables by placing the in a weighted, normalized single achievement function 
          - achievement function: variables that penalizes objective function
        - contoh
      - Chebyshev (Minmax Goal Programming) 
        - uses $L_{\infty}$ distance metric
          - $L_{\infty}$ adalah sebuah norma, dimana norma biasanya disebut sebagai dimensi vektor [definisi lengkap](https://rorasa.wordpress.com/2012/05/13/l0-norm-l1-norm-l2-norm-l-infinity-norm/)
          - where p is the $L_p$ norm
          - $\|x\|_p = \sqrt[p]{\Sigma_i |x_i|^p}$
            - $L_1$ norm: 
              - SAD (sum of absolute distance)
              - MAE (mean absolute error)
            - $L_2$ norm: 
              - most popular norm 
              - SSD (Sum of squared distance)
              - MSE (Mean Squared Error )
              - Euclidean Distance
              - $\|x\|_2 = \sqrt{\Sigma_i x_i^2}$
            - $L_{\infty} norm$
              - maximum entrires magnitude of that vector. 
              - $\|x\|_{\infty} = \sqrt{\Sigma_i x_i^\infty}$
              - $\|x\|_{\infty} = max(|x_i|)$
        - achieves balance between achievement function and objective function 
        - can find optimal soultion for linear models, that don't have extreme point in decision space
        - ![](img/minmaxgp.png)
    - Decision Based 
      - Fuzzy 
      - Integer and Binary 
      - Fractional 
  - Pareto efficiency 
    - objective: objective not improved without worsening the value of other objective (objective = goal)
