# Contributing to GesturaSlide

Thank you for your interest in contributing to the GesturaSlide project! We're excited to have you help improve gesture-based presentation control. This document provides guidelines and information to help you get started with contributing to this innovative computer vision application.

## Code of Conduct

This project adheres to a Code of Conduct to ensure a welcoming and inclusive environment for all contributors. Please take a moment to [read the full text](./CODE_OF_CONDUCT.md) to understand the expectations for participation.

## Our Development Process

We use GitHub to manage our project, track issues, discuss feature requests, and review pull requests. Our process is designed to be transparent and collaborative, ensuring that every contribution is valuable and aligns with the project's goals.

## Getting Started: Setting Up Your Development Environment

Before you can start contributing, you need to set up the project on your local machine. Please follow the detailed setup instructions in the main [README.md](README.md) file. Here's a quick checklist with development-specific steps:

1. **Fork and Clone** the repository to your local machine.
2. **Create a Virtual Environment** by running `python -m venv venv`.
3. **Activate the Virtual Environment:**
   * On Windows: `.\venv\Scripts\activate`
   * On macOS/Linux: `source venv/bin/activate`
4. **Install Dependencies** by running `pip install -r requirements.txt`.
5. **Test the Installation** by running `python main.py` to ensure everything works correctly.
6. **Prepare Development Tools:**
   * Install any code editor or IDE of your choice (VS Code, PyCharm, etc.).
   * Ensure git is installed and configured on your machine.

## How to Contribute

We welcome contributions in various forms, including bug fixes, new features, performance optimizations, and documentation improvements. Please follow the steps below for a smooth contribution process.

### 1. Fork the Repository and Create a Branch

* Fork this repository to your GitHub account.
* Create a new branch from the `master` branch for your work. Use a descriptive name for your branch, for example:
  * `feature/add-click-detection` (new feature for gesture-based clicking)
  * `fix/camera-initialization-error` (bug fix)
  * `docs/improve-gesture-guide` (documentation improvement)
  * `perf/optimize-hand-tracking` (performance optimization)

### 2. Make Your Changes

* **Code Structure:** The application logic is primarily in `main.py`. Understand the existing gesture detection algorithms before making changes.
* **Gesture Logic:** When modifying gesture recognition, ensure finger counting and distance calculations remain accurate.
* **Configuration:** Test with different `smooth_factor`, `min_detection_confidence`, and `cooldown` values to ensure robustness across various hardware configurations.
* **Dependencies:** Keep the `requirements.txt` file updated if you add new packages. Use `pip freeze > requirements.txt` to generate the updated list after installing new dependencies.
* **Comments and Documentation:** Add clear comments explaining complex gesture calculations or mathematical operations.

### 3. Test Your Changes Thoroughly

Before submitting a pull request, it is crucial to test your changes to ensure they work as expected and don't introduce new issues. Please verify the following:

* **Hand Detection Accuracy:**
  * Test gesture recognition in different lighting conditions.
  * Verify that both single-hand and two-hand gestures work correctly.
  * Test with different hand sizes and distances from the camera.
* **Cursor Movement:**
  * Ensure smooth and responsive cursor movement across various screen resolutions.
  * Test cursor movement on different Windows/OS operating systems.
* **Slide Navigation:**
  * Verify that 3-finger gestures reliably trigger "next slide" commands.
  * Verify that 2-finger gestures reliably trigger "previous slide" commands.
  * Test rapid gesture sequences to ensure the cooldown mechanism works properly.
* **Zoom Functionality:**
  * Test two-hand zoom in and zoom out operations.
  * Verify zoom commands work in multiple applications (browsers, presentation software, etc.).
* **Performance:**
  * Monitor CPU and memory usage while the application is running.
  * Ensure the application runs smoothly at 30+ FPS on your hardware.
* **Edge Cases:**
  * Test with partial hand visibility (e.g., hand partially off-screen).
  * Test with occluded fingers (e.g., fingers overlapping).
  * Test with multiple people in the frame.

### 4. Submit a Pull Request (PR)

* **Commit Your Changes:** Write clear and concise commit messages that describe your changes.
  * Example: `Fix: Improve hand detection confidence threshold accuracy`
  * Example: `Feat: Add click detection gesture with closed fist`
* **Push to Your Fork:** Push your changes to the feature branch on your forked repository.
* **Open a Pull Request:** Navigate to the original repository on GitHub and open a new pull request against the `master` branch.
* **PR Description:** Provide a clear and detailed description of your changes in the PR, including:
  * What problem you're solving or what feature you're adding.
  * How you've tested the changes.
  * Any performance implications.
  * Screenshots or videos if your change includes visual or behavioral improvements.
  * Link to any relevant issues you're addressing.

We will review your pull request and provide feedback as soon as possible. Thank you for your contribution!

## Reporting Issues

If you find a bug or have a suggestion for a new feature, please open an issue on GitHub. When reporting a bug, please provide:

* A clear and descriptive title.
* Detailed steps to reproduce the issue.
* The expected behavior versus the actual behavior.
* Information about your environment (OS, Python version, camera model, lighting conditions), as gesture recognition can be sensitive to environmental factors.
* Any relevant error messages, logs, or screenshots.
* Your hardware specifications (CPU, RAM) as performance can vary significantly.

## Areas of Contribution

If you're looking for ideas, here are some areas where we would particularly appreciate contributions:

1. **Gesture Recognition Improvements:**
   * Implementing new gestures (e.g., thumbs up for fullscreen, peace sign for pause).
   * Improving detection accuracy for challenging hand positions.
   * Adding support for left-handed and right-handed preference configurations.
   * Implementing gesture profiles for different presentations or applications.

2. **Performance Optimization:**
   * Optimizing hand landmark calculations for lower-latency cursor movement.
   * Reducing CPU usage while maintaining detection accuracy.
   * Implementing multi-threading for better utilization of multi-core processors.
   * Profiling and benchmarking gesture recognition performance.

3. **User Experience Enhancements:**
   * Adding on-screen gesture hints or visual feedback.
   * Implementing calibration tools for individual users.
   * Creating a settings/configuration GUI instead of hardcoded parameters.
   * Adding logging or debug visualization modes.

4. **Compatibility and Robustness:**
   * Testing and fixing compatibility across different Python versions.
   * Supporting different camera devices and resolutions.
   * Improving performance on lower-end hardware (e.g., Raspberry Pi).
   * Adding graceful error handling for missing camera or hardware issues.

5. **Documentation and Examples:**
   * Creating tutorial videos demonstrating each gesture.
   * Writing detailed guides for different presentation software.
   * Providing configuration examples for specific use cases.
   * Adding troubleshooting guides for common issues.

6. **Testing:**
   * Setting up automated testing frameworks for gesture recognition.
   * Creating test cases for edge cases and error scenarios.
   * Developing performance benchmark tests.

## Development Best Practices

* Keep your code clean and readable.
* Follow PEP 8 style guidelines for Python code.
* Test your changes on different hardware configurations if possible.
* Ensure backward compatibility with existing code.
* Document your changes with comments explaining complex logic.
* Keep commits small and focused on single features or fixes.

## License

By contributing to this project, you agree that your contributions will be licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for the full terms.

## Questions or Need Help?

If you have questions or need assistance while contributing, please feel free to open an issue or discussion on GitHub. We're here to help!

---

Thank you for helping make GesturaSlide better!
