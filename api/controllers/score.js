const express = require("express");
const router = express();
const Score = require("../models/score");

/* Get all scores */
// router.get("/", async (req, res) => {
//   try {
//     const scores = await Score.find();
//     res.json(scores);
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

/* Get one score */
// router.get("/:id", getScore, (req, res) => {
//   res.send(res.score);
// });

/* Create score */
router.post("/", async (req, res) => {
  console.log(req.body);
  const { gamertag, score: newScore } = req.body;
  const score = new Score({
    gamertag,
    score: newScore,
  });

  try {
    const newScore = await score.save();
    res.status(201).json({ success: newScore }); // status 201 specifically means something was successfully created
  } catch (err) {
    res.status(400).json({ error: err.message }); // status 400 means bad data was recieved
  }
});

/* Update score */
// router.patch("/:id", getScore, async (req, res) => {
//   /* If new name was sent, update score name */
//   if (req.body.name) res.score.name = req.body.name;
//   /* If new price was sent, update score price */
//   if (req.body.price) res.score.price = req.body.price;

//   try {
//     const updatedScore = await res.score.save();
//     res.status(200).json({ score: updatedScore });
//   } catch (err) {
//     res.status(400).json({ error: err.message });
//   }
// });

/* Delete score */
// router.delete("/:id", getScore, async (req, res) => {
//   try {
//     let removedId = res.score._id.toString();
//     await res.score.remove();
//     res.status(200).json({ message: "Ydelse slettet.", id: removedId });
//   } catch (err) {
//     res.status(500).json({ error: err.message });
//   }
// });

/* Middleware */
async function getScore(req, res, next) {
  let score;

  try {
    score = await Score.findById(req.params.id);
    if (score == null)
      return res.status(404).json({ message: "Score not found." });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }

  res.score = score;
  next();
}

module.exports = router;
