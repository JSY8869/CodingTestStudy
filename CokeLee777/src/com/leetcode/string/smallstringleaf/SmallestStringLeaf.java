package com.leetcode.string.smallstringleaf;

public class SmallestStringLeaf {

    private String ans = "z".repeat(8500);

    private void dfs(TreeNode node, String tmp){
        char alphabet = (char) (node.val + 97);
        tmp += alphabet;
        // TODO : 자식노드가 존재하지 않고 사전순으로 앞선다면 값 변경
        if(node.left == null && node.right == null) {
            String reverseTmp = new StringBuffer(tmp).reverse().toString();
            if(reverseTmp.compareTo(ans) < 0){
                ans = reverseTmp;
                return;
            }
        }

        // TODO : 자식 노드로 방문
        if(node.left != null) dfs(node.left, tmp);
        if(node.right != null) dfs(node.right, tmp);
    }

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, "");
        return ans;
    }
}
