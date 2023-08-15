const mongoose = require("mongoose");

const scoreSchema = new mongoose.Schema({
  gamertag: {
    type: String,
    required: true,
  },
  score: {
    type: Number,
    required: true,
  },
});

module.exports = mongoose.model("Score", scoreSchema);
