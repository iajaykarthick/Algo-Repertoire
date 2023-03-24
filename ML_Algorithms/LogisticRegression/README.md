We could approach the classification problem ignoring the fact that y is discrete-valued, and use our old linear regression algorithm to try to predict y given x. However, it is easy to construct examples where this method performs very poorly. Intuitively, it also doesn’t make sense for $h​_\theta(x)$ to take values larger than 1 or smaller than 0 when we know that $y \in {0, 1}$. To fix this, let’s change the form for our hypotheses 
$h_\theta(x)$ to satisfy $0 \leq h_\theta(x) \leq 1$. This is accomplished by plugging $\theta^T x$ into the Logistic Function.

## Logistic Function:

### History
1830-1850 - under the guidance of Adolphe Quetelet,  Pierre François Verhulst developed the logistic function. It was developed for the purpose of modeling population growth.
1833 - logistic function was independently developed in chemistry as a model of autocatalysis by Wihelm Ostwald.

### Logistic Function derived from Logistic Differential Equation

![](imags/../images/logistic_eq1.jpg)
![](imags/../images/logistic_eq2.jpg)
![](imags/../images/logistic_eq3.jpg)
![](imags/../images/logistic_eq4.jpg)
![](imags/../images/logistic_eq5.jpg)
![](imags/../images/logistic_eq6.jpg)


![](images/code.png)