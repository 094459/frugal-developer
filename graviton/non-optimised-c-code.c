#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

// Inefficient scalar computation
void compute_scalar(std::vector<float>& data) {
    for (size_t i = 0; i < data.size(); i++) {
        data[i] = data[i] * data[i] + sinf(data[i]);  // Scalar operation
    }
}

int main() {
    std::vector<float> data(1000000, 1.23f);

    auto start = std::chrono::high_resolution_clock::now();
    compute_scalar(data);
    auto end = std::chrono::high_resolution_clock::now();

    std::cout << "Scalar Execution Time: "
              << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count()
              << " ms\n";
    return 0;
}
