
#include<bits/stdc++.h>
using namespace std;

#define PI 3.1415

double circumference(double r)
{
	double cir = 2*PI*r;
	return cir;
}

// driver function
int main()
{
double r = 5;
cout << "Circumference = "
	<< circumference(r);
return 0;
}
