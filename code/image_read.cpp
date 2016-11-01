#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void add_image(char *filename){
  char name[1000];
  char data[100];
  strcpy(name,"../training_data/face/an2i/");
  strcat(name,filename);
  strcat(name,".pgm");
  cout << name<<endl;
  //ifstream infile; 
  int row = 0, col = 0, numrows = 0, numcols = 0;
  ifstream infile(name);
  stringstream ss;
  string inputLine = "";

  // First line : version
  getline(infile,inputLine);
  cout << inputLine<<endl;
  cout << "net"<<endl;
  if(inputLine.compare("P2") != 0) cerr << "Version error" << endl;
  else cout << "Version : " << inputLine << endl;

  // Second line : comment
  getline(infile,inputLine);
  cout << "Comment : " << inputLine << endl;

  // Continue with a stringstream
  ss << infile.rdbuf();
  // Third line : size
  ss >> numcols >> numrows;
  cout << numcols << " columns and " << numrows << " rows" << endl;

  int array[numrows][numcols];

  // Following lines : data
  for(row = 0; row < numrows; ++row)
    for (col = 0; col < numcols; ++col) ss >> array[row][col];

  // Now print the array to see the result
  for(row = 0; row < numrows; ++row) {
    for(col = 0; col < numcols; ++col) {
      cout << array[row][col] << " ";
    }
    cout << endl;
  }
  infile.close();
}
 // infile.close();
  //FILE *my_file=fopen("../training_data/face/an2i/%s",filename,"r");
  



int main(){
  char filename[100];
  cin>>filename;
  add_image(filename);
  return 0;
}
