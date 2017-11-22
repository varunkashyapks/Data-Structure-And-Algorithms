import java.io.*;
import java.nio.file.*;
import java.util.*;


class WordCount {
 
  private static Map<String, Integer> wordCount = new HashMap<String, Integer>();
  private static int numberOfWords;

  public static void main(String[] args) {
    try {
      numberOfWords = Integer.parseInt(args[0]);
      retrieveFiles(args);
      printResult();
    } catch (Exception exception) {
      System.out.println("Please enter a valid input.\nExample:");
      System.out.println("java WordCount 5 /test/ /test-two/new.txt");
    }
  }


  public static void retrieveFiles(String[] paths) {
    for (int i = 1; i < paths.length; i++) {
      if (paths[i].charAt(0) == '/') {
        paths[i] = "." + paths[i];
      }
      searchDirectory(paths[i]);
    }
  }

  private static void searchDirectory(String path) {
    try {
      Files.walk(Paths.get(path))
        .filter(Files::isRegularFile)
        .parallel()
        .forEach(WordCount::processFilePath);
    } catch (Exception e) {
      processFilePath(path);
    }
  }

  private static <T> void processFilePath(T path) {
    try {
      File file = obtainFile(path.toString());
      BufferedReader reader = new BufferedReader(new FileReader(file));
      processFile(reader);
    } catch (Exception exception) {
      System.out.println("Error parsing path.");
      System.exit(1);
    }
  }

  private static File obtainFile(String fileName) {
    File file = new File(fileName);
    try {
      if (!file.isFile())
        throw new IOException("File/Directory does not exist");
    } catch (Exception e) {
      e.printStackTrace();
      System.out.println("Please enter a valid input.\nExample:");
      System.out.println("java WordCount 5 /test/ /test-two/new.txt");
      System.exit(1);
    }
    return file;
  }

 
  private static void processFile(BufferedReader reader) {
    String line;
    try {
      while ((line = reader.readLine()) != null) {
        countWords(line);
      }
      reader.close();
    } catch (Exception e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

 
  private static void countWords(String content) {
    String[] words = content.split("\\s+");
    for (String word : words) {
      word = word.toLowerCase().replaceAll("[^a-z-']", "");
      if (word.isEmpty()) { continue; } // Skip if word is empty. Edge case after removing punctuation.
      incrementCount(word);
    }
  }

  private synchronized static void incrementCount(String word) {
    if (wordCount.get(word) == null) {
      wordCount.put(word, 0);
    }
    wordCount.put(word, wordCount.get(word) + 1);
  }

  
  public static void printResult() {
    wordCount.entrySet().stream()
      .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
      .limit(numberOfWords)
      .forEach(entry -> { formatResult(entry); });
  }
  private static void formatResult(Map.Entry<String, Integer> entry) {
    String result = "Word '<" + entry.getKey() + ">' occured <" + entry.getValue() + "> times";
    System.out.println(result);
  }
}