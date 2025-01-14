class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> heap;
        vector<int> top_k;
        unordered_map<int, int> freqs;

        for (const auto& num : nums) {
            freqs[num] += 1;
        }

        for (const auto& [n, f] : freqs) {
            heap.push({f, n});
        }

        while (!heap.empty() && k > 0) {
            top_k.emplace_back(heap.top().second);
            heap.pop();
            k -= 1;
        }

        return top_k;
    }
};
