import java.util.*; 
import java.io.*;

class Main {  
  public static String LongestWord(String sen) { 
  
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
       String result = "";
       String[] senArray = sen.replaceAll("[^a-zA-Z ]", "").toLowerCase().split("\\s+");
       
       result = senArray[0];
       for (int i = 1; i < senArray.length; i++)
       {
           if (result.length() < senArray[i].length())
           {
               result = senArray[i];
           }
       }
       
       return result;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(LongestWord(s.nextLine())); 
  }   
  
}Longest Word

