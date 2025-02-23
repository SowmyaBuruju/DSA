#include <iostream>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder,
                                   vector<int>& postorder) {
        int numOfNodes = preorder.size();
        return constructTree(0, numOfNodes - 1, 0, preorder, postorder);
    }

private:
    TreeNode* constructTree(int preStart, int preEnd, int postStart,
                            vector<int>& preorder, vector<int>& postorder) {
        if (preStart > preEnd) return NULL;

        if (preStart == preEnd) {
            return new TreeNode(preorder[preStart]);
        }

        int leftRoot = preorder[preStart + 1];

        int numOfNodesInLeft = 1;
        while (postorder[postStart + numOfNodesInLeft - 1] != leftRoot) {
            numOfNodesInLeft++;
        }

        TreeNode* root = new TreeNode(preorder[preStart]);

        root->left = constructTree(preStart + 1, preStart + numOfNodesInLeft,
                                   postStart, preorder, postorder);

        root->right =
            constructTree(preStart + numOfNodesInLeft + 1, preEnd,
                          postStart + numOfNodesInLeft, preorder, postorder);

        return root;
    }
};

// Function to print the tree in Preorder format
void printPreorder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    printPreorder(root->left);
    printPreorder(root->right);
}

// Function to free allocated memory
void deleteTree(TreeNode* root) {
    if (!root) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

// Test cases
void runTests() {
    Solution sol;

    // Test Case 1
    vector<int> preorder1( {1, 2, 4, 5, 3, 6, 7} );
    vector<int> postorder1( {4, 5, 2, 6, 7, 3, 1} );
    TreeNode* root1 = sol.constructFromPrePost(preorder1, postorder1);
    cout << "Test Case 1 Preorder Output: ";
    printPreorder(root1);
    cout << endl;
    deleteTree(root1);

    // Test Case 2 (Single Node)
    vector<int> preorder2( {1} );
    vector<int> postorder2( {1} );
    TreeNode* root2 = sol.constructFromPrePost(preorder2, postorder2);
    cout << "Test Case 2 Preorder Output: ";
    printPreorder(root2);
    cout << endl;
    deleteTree(root2);

    // Test Case 3 (Left Skewed Tree)
    vector<int> preorder3( {1, 2, 3, 4} );
    vector<int> postorder3( {4, 3, 2, 1} );
    TreeNode* root3 = sol.constructFromPrePost(preorder3, postorder3);
    cout << "Test Case 3 Preorder Output: ";
    printPreorder(root3);
    cout << endl;
    deleteTree(root3);

    // Test Case 4 (Right Skewed Tree)
    vector<int> preorder4( {1, 2, 3, 4} );
    vector<int> postorder4( {4, 3, 2, 1} );
    TreeNode* root4 = sol.constructFromPrePost(preorder4, postorder4);
    cout << "Test Case 4 Preorder Output: ";
    printPreorder(root4);
    cout << endl;
    deleteTree(root4);

    // Test Case 5 (Balanced Tree)
    vector<int> preorder5( {1, 2, 4, 3, 5} );
    vector<int> postorder5( {4, 2, 5, 3, 1} );
    TreeNode* root5 = sol.constructFromPrePost(preorder5, postorder5);
    cout << "Test Case 5 Preorder Output: ";
    printPreorder(root5);
    cout << endl;
    deleteTree(root5);
}

int main() {
    runTests();
    return 0;
}
