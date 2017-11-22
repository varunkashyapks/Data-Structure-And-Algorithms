import java.io.IOException;
import java.util.List;


public class nearduplicates {
	public static void main(String[] args) throws NumberFormatException, IOException {
		if(args.length < 5) throw new IllegalArgumentException(
				"Enter <folder> <num permutations> <num bands> <similarity threshold> <doc name>");
		MinHash mh = new MinHash(args[0], Integer.parseInt(args[1]));
		int[][] hashMtx = mh.minHashMatrix();
		String[] docNames = mh.allDocs();
		LSH lsh = new LSH(hashMtx, docNames, Integer.parseInt(args[2]));
		List<String> nearDuplicates = lsh.nearDuplicatesOf(args[4]);
		
		int FP = 0;
		for(String s : nearDuplicates) {
			
			double sim = mh.exactJaccard(args[4], s);
			if(sim > Double.parseDouble(args[3])) {
				System.out.println(s);
			} else {
				FP++;
			}
		}
		
		System.out.println("Number of false positives: " + FP);
	}

}