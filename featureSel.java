import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class featureSel {
    public static void main(String []args) {
        String csvFile = "feature.csv";
        int[] indexes = {5, 1, 4,3,2};
        selected(csvFile,indexes);
    }
       public static  void selected ( String b,int[] x ) {

            String csvFile = b;
            String line = "";
            String cvsSplitBy = ",";

            int[] indexes = x;//feature indexes and class variable(first index)
            ArrayList<Integer> classVariable = new ArrayList<>();
            ArrayList<String> featureSet = new ArrayList<>();
            //places.add("Buenos Aires");


            try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
                br.readLine();
                while ((line = br.readLine()) != null) {

                    // use comma as separator
                    String[] columns = line.split(cvsSplitBy);
                    int label = Integer.parseInt(columns[indexes[0]]);
                    classVariable.add(label); // added class variable to the seperate list
                    String rows = "";
                    for (int i = 1; i < indexes.length; i++) {
                        rows = rows + columns[indexes[i]]; // string concatenation , fature set concat

                    }
                    featureSet.add(rows); // feature set concat as a string and added to string arraylist
                    //System.out.println(columns[2] + " " + columns[3]);

                }
                //for (Integer n : classVariable ){
                //    System.out.print(n+"  ");
                //}
                //System.out.println();
                //for (String n : featureSet ){
                //    System.out.print(n+ "  ");
                //}

            }
            catch (IOException e) {
                e.printStackTrace();
            }
            // map -> dataset
            Map<String, List<Integer>> dataset = new HashMap<>();
            List<Integer> labels = new ArrayList<>();
            labels.add(classVariable.get(0));
            dataset.put(featureSet.get(0), labels);

            for (int i = 1; i < classVariable.size(); i++) {
                List<Integer> temp = new ArrayList<>();
                if (dataset.containsKey(featureSet.get(i))) {
                    temp = dataset.get(featureSet.get(i));
                    temp.add(classVariable.get(i));
                } else {
                    temp.add(classVariable.get(i));
                    dataset.put(featureSet.get(i), temp);
                }

            }
            int inconsistencyTotal = 0;
            for (Map.Entry<String, List<Integer>> entry : dataset.entrySet()) {
                String key = entry.getKey();
                List<Integer> values = entry.getValue();
                Collections.sort(values);
                int counter = 1;
                int max = 0;
                boolean same = true;
                int inconsistency = 0;

                for (int i = 1; i < values.size(); i++) {
                    if (values.get(i) == values.get(i - 1)) { // same char check
                        counter++;
                        if ((i + 1) == values.size() && counter > max)
                            max = counter;
                    } else { // different char check
                        if (counter > max) {
                            max = counter;
                            counter = 1;
                            same = false;
                        }


                    }
                    if (same) {
                        inconsistency = 0;
                    } else
                        inconsistency = values.size() - max;

                }

                System.out.println("Key = " + key);
                System.out.println("Values = " + values);
                System.out.println("inconsistency = " + inconsistency);
                inconsistencyTotal += inconsistency;
            }
            System.out.println("inconsistencyTotal = " + inconsistencyTotal);
            System.out.println("classVariable = " + classVariable.size());
            double a = classVariable.size();
            double rate = inconsistencyTotal / a;
            System.out.printf("inconsistencyRate = %.5f ", rate);

        }
    }
