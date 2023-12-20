public class Kata {
  public static int findEvenIndex(int[] arr) {
    int left_sum = 0;
    
    for (int i = 0; i < arr.length; ++i) {  
      int temp = 0;
      for (int ck = i+1; ck < arr.length; ++ck) {
        temp += arr[ck];
      }
      
      if (temp == left_sum) return i;
      
      left_sum += arr[i];
    }
    
    return -1;
  }
}
