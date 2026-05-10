# Day 7 — Reflection

## What classical methods detect well

### 1. FFT / Spectrum Analysis (Frequency Domain)
FFT-based analysis effectively detects Tone Jammers because they create sharp, high-energy spikes at specific frequencies. It also detects Barrage Jammers by showing a broad increase in the noise floor across a wide frequency range.

### 2. Amplitude / Energy Thresholding (Time Domain)
Time-domain thresholding works well for Pulsed and Reactive Jammers because they produce sudden high-energy bursts and large amplitude spikes that easily exceed normal signal levels.

---

## Where classical methods fail

### 1. Time-Domain Analysis
Time-domain thresholding struggles with Tone and Barrage Jammers because their interference is continuous and does not create sudden amplitude spikes. They may appear similar to normal background noise.

### 2. Frequency-Domain Analysis
FFT analysis struggles with Pulsed and Reactive Jammers because their short bursts spread energy across many frequencies, making them appear like broadband noise rather than targeted interference.

---

## What patterns feel hidden

The main hidden pattern is that jammer behavior changes depending on the observation domain. Jammers concentrated in time become difficult to identify in the frequency domain, while jammers concentrated in frequency become difficult to identify in the time domain. The true jammer pattern becomes clear only when both domains are analyzed together.