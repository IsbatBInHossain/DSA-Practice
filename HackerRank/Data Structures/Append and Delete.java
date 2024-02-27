import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static String appendAndDelete(String s, String t, int k) {
    // Write your code here
    int common = 0;
    String shorter = (s.length() < t.length()) ? s : t;
    String longer = (s.length() >= t.length()) ? s : t;
    for (int i = 0; i<shorter.length(); i++){
        if (shorter.charAt(i) == longer.charAt(i)){
            common++;
        } else break;
    }
    int diff = s.length() + t.length() - 2*common;
    if (k>= s.length() + t.length()){
        return "Yes";
    }
    
    if (k>= diff && (k - diff) %2 == 0){
        return "Yes";
    } 
    return "No";

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String t = bufferedReader.readLine();

        int k = Integer.parseInt(bufferedReader.readLine().trim());

        String result = Result.appendAndDelete(s, t, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
