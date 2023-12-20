public class Maskify {
  public static String maskify(String str) {
    char[] strmask = str.toCharArray();
    
    if (strmask.length > 4) {
      for (int i = 0; i < strmask.length-4; ++i) {
        strmask[i] = '#';
      }
      return new String(strmask);
    } else {
      return new String(strmask);
    }
  }
}
