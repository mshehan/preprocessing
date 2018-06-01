package cmps142_hw4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.lang.Math;

public class LogisticRegression {

		private double log2 = Math.log(2);

        /** the learning rate */
        private double rate=0.01;

        /** the weights to learn */
        private double[] weights;

        /** the number of iterations */
        private int ITERATIONS = 200;

        /** TODO: Constructor initializes the weight vector. Initialize it by setting it to the 0 vector. **/
        public LogisticRegression(int n) { // n is the number of weights to be learned
        	weights = new double[n];
        	for (int i = 0; i < n; i++) {
        		weights[i] = 0;
        	}
        }

        /** TODO: Implement the function that returns the L2 norm of the weight vector **/
        private double weightsL2Norm(){
        	double norm = 0;
        	for(int i = 0; i < weights.length; i++) {
        		norm += Math.pow(weights[i], 2);
        	}

        	return Math.sqrt(norm);
        }

        /** TODO: Implement the sigmoid function **/
        private static double sigmoid(double z) {
        	return 1 / (1 + Math.exp(-1*z)); // note: z is already negative
        }

        /** TODO: Helper function for prediction **/
        /** Takes a test instance as input and outputs the probability of the label being 1 **/
        /** This function should call sigmoid() **/
        private double probPred1(double[] x) {
        	double exponent = 0;
        	for (int i = 0; i < weights.length; i++) {
        		exponent += weights[i] * x[i]; 
        	}
        	return sigmoid(exponent);
        }

        /** TODO: The prediction function **/
        /** Takes a test instance as input and outputs the predicted label **/
        /** This function should call probPred1() **/
        public int predict(double[] x) {
        	double prob = probPred1(x);
        	//System.out.println(prob);
        	return prob >= 0.5 ? 1 : 0;
        }

        /** This function takes a test set as input, call the predict() to predict a label for it, and prints the accuracy, P, R, and F1 score of the positive class and negative class and the confusion matrix **/
        public void printPerformance(List<LRInstance> testInstances) {
            double acc = 0;
            double p_pos = 0, r_pos = 0, f_pos = 0;
            double p_neg = 0, r_neg = 0, f_neg = 0;
            int TP=0, TN=0, FP=0, FN=0; // TP = True Positives, TN = True Negatives, FP = False Positives, FN = False Negatives

            // TODO: write code here to compute the above mentioned variables
            for(int i = 0; i < testInstances.size(); i++) {
                LRInstance instance = testInstances.get(i);
                double prediction = predict(instance.x);
                if(instance.label == prediction && instance.label == 0){
                    TN += 1;
                }
                if(instance.label == prediction && instance.label == 1){
                    TP += 1;
                }
                if(instance.label != prediction && instance.label == 0) {
                    FP += 1;
                }
                if(instance.label != prediction && instance.label == 1) {
                    FN += 1;
                }
            }
            acc = ((double)TP+TN)/testInstances.size();
            p_pos = ((double)TP/(double)(TP+FP));
            p_neg = ((double)TN/(double)(TN+FN));
            r_pos = ((double)TP/(double)(TP+FN));
            r_neg = ((double)TN/(double)(TN+FP));
            f_pos = (2 * p_pos * r_pos) / (p_pos + r_pos);
            f_neg = (2 * p_neg * r_neg) / (p_neg + r_neg);
            System.out.println("Accuracy="+acc);
            System.out.printf("P, R, and F1 score of the positive class = %.2f %2.2f %2.2f\n",p_pos,r_pos,f_pos);
            System.out.printf("P, R, and F1 score of the positive class = %.2f %2.2f %2.2f\n",p_neg, r_neg, f_neg);
            System.out.println("Confusion Matrix");
            System.out.println(TP + "\t" + FN);
            System.out.println(FP + "\t" + TN);
        }

        public void train(List<LRInstance> instances) {
            for (int n = 0; n < ITERATIONS; n++) {
                double lik = 0.0; // Stores log-likelihood of the training data for this iteration
                
                for (int i = 0; i < instances.size(); i++) {
                	// System.out.print("Instance #" + i);
                    // TODO: Train the model
                    LRInstance instance = instances.get(i);
                    double predicted_label = predict(instance.x);
                    
                    for (int feat = 0; feat < weights.length; feat++) {
                    	weights[feat] = weights[feat] + 
                    		(rate * instance.x[feat] * (instance.label - predicted_label));
                        lik += weights[feat]*instance.x[feat]*instance.label;
                    }
                    //used the formula for log likelihood found here:
                    // https://www.statlect.com/fundamentals-of-statistics/logistic-model-maximum-likelihood
                    // TODO: Compute the log-likelihood of the data here. Remember to take logs when necessary
                    lik += -Math.log(probPred1(instance.x));
				}
                System.out.printf("iteration:%5d %2s lik:%13f\n", n, " ", lik);
            }
        }

        public static class LRInstance {
            public int label; // Label of the instance. Can be 0 or 1
            public double[] x; // The feature vector for the instance

            /** TODO: Constructor for initializing the Instance object **/
            public LRInstance(int label, double[] x) {
            	this.x = x;
            	this.label = label;
            }
        }

        /** Function to read the input dataset **/
        public static List<LRInstance> readDataSet(String file) throws FileNotFoundException {
            List<LRInstance> dataset = new ArrayList<LRInstance>();
            Scanner scanner = null;
            try {
                scanner = new Scanner(new File(file));

                while(scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    if (line.startsWith("...")) { // Ignore the header line
                        continue;
                    }
                    String[] columns = line.replace("\n", "").split(",");

                    // every line in the input file represents an instance-label pair
                    int i = 0;
                    double[] data = new double[columns.length - 1];
                    for (i=0; i < columns.length - 1; i++) {
                        data[i] = Double.valueOf(columns[i]);
                    }
                    int label = Integer.parseInt(columns[i]); // last column is the label
                    LRInstance instance = new LRInstance(label, data); // create the instance
                    dataset.add(instance); // add instance to the corpus
                }
            } finally {
                if (scanner != null)
                    scanner.close();
            }
            return dataset;
        }


        public static void main(String... args) throws FileNotFoundException {
            List<LRInstance> trainInstances = readDataSet("HW3_TianyiLuo_train.csv");
            List<LRInstance> testInstances = readDataSet("HW3_TianyiLuo_test.csv");

            // create an instance of the classifier
            int d = trainInstances.get(0).x.length; 
            LogisticRegression logistic = new LogisticRegression(d);

            logistic.train(trainInstances);

            System.out.println("Norm of the learned weights = "+logistic.weightsL2Norm());
            System.out.println("Length of the weight vector = "+logistic.weights.length);

            // printing accuracy for different values of lambda
            System.out.println("-----------------Printing train set performance-----------------");
            logistic.printPerformance(trainInstances);

            System.out.println("-----------------Printing test set performance-----------------");
            logistic.printPerformance(testInstances);
        }

    }

