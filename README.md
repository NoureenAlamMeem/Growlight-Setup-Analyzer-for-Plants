# 🌱 Plant Growth Analyzer

This project is based on my personal hobby of **growing and taking care of house plants**.  
I often wondered if my plants were getting the right amount of light, so I built a small tool to **analyze plant growth conditions** like light, hours, and electricity cost.

---

## 🚀 What it does

- Shows available plants from a dataset  
- Displays plant-specific light requirements  
- Evaluates your setup (watt, hours, lux)  
- Calculates yearly electricity cost  
- Gives a score and feedback  

---

## ⚙️ How to run

```
uv run -m plantgrowth <command>
```

---

## 📋 Commands

### 1. List all plants

```
uv run -m plantgrowth list-plants
```

**Output:**

![List Plants](./assets/list-plants.png)

---

### 2. Get plant information

```
uv run -m plantgrowth plant-info pothos
```

**Output:**

![Plant Info](./assets/plant-info.png)

---

### 3. Check plant setup

```
uv run -m plantgrowth check --plant pothos --watt 15 --hours 12 --price 0.38
```

**Output:**

![Check Output](./assets/check.png)

---

## 🧠 Idea behind the project

As someone who enjoys keeping indoor plants, I wanted a simple way to **understand if my plants are getting enough light** and how much it costs to maintain them.

---

## ✅ Features

- Simple CLI interface  
- CSV-based plant dataset  
- Light & lux estimation  
- Scoring system (Good / Poor / Excellent)  
- Cost calculation  

---

## 📌 Notes

- Lux is estimated from wattage (simplified model)  
- Designed for learning and experimentation  

---

## 👤 Author

Built as part of a Python project, inspired by my hobby of **growing house plants** 🌱
