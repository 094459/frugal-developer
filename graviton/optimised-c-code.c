#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <arm_neon.h>

// Optimized SIMD computation using ARM NEON
void compute_neon(std::vector<float>& data) {
    size_t i = 0;
    size_t len = data.size();
    
    // Process 4 elements at a time using NEON
    for (; i + 3 < len; i += 4) {
        float32x4_t vec = vld1q_f32(&data[i]);    // Load 4 floats
        vec = vmulq_f32(vec, vec);               // Square each element
        vec = vaddq_f32(vec, vsin_f32(vec));     // Add sin(element)
        vst1q_f32(&data[i], vec);                // Store back results
    }

    // Handle any remaining elements (scalar processing)
    for (; i < len; i++) {
        data[i] = data[i] * data[i] + sinf(data[i]);
    }
}

int main() {
    std::vector<float> data(1000000, 1.23f);

    auto start = std::chrono::high_resolution_clock::now();
    compute_neon(data);
    auto end = std::chrono::high_resolution_clock::now();

    std::cout << "NEON Execution Time: "
              << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count()
              << " ms\n";
    return 0;
}
