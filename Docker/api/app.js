import express from "express";

const app = express();
const port = 4000;

app.get("/", (req, res) => {
  res.status(200).json([
    {
      id: 1,
      firstName: "Ake",
      lastName: "Martins",
      location: "Abuja",
    },
    {
      id: 2,
      firstName: "Bukola",
      lastName: "Oladele",
      location: "Unknown",
    },
    {
      id: 3,
      firstName: "Najiu",
      lastName: "Danesi",
      location: "Kaduna",
    },
    {
      id: 4,
      firstName: "Martha",
      lastName: "Martha",
      location: "Unknown",
    },
    {
      id: 5,
      firstName: "Olasunkanmi",
      lastName: "Adebiyi",
      location: "Ogun",
    },
    {
      id: 6,
      firstName: "Oyinkansola",
      lastName: "Oyin",
      location: "Unknown",
    },
  ]);
});


app.listen(port, () => {
    console.log(`Your app is running on port ${port} in a classified location`);
})
