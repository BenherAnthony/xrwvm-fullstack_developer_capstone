import React, { useEffect, useState } from "react";

function Home() {
  const [dealers, setDealers] = useState([]);

  useEffect(() => {
    fetch("/djangoapp/get_dealerships")
      .then((res) => res.json())
      .then((data) => {
        setDealers(data.dealerships || []);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dealerships</h1>

      {dealers.length === 0 ? (
        <p>No dealerships available</p>
      ) : (
        dealers.map((dealer) => (
          <div
            key={dealer.id}
            style={{
              border: "1px solid #ccc",
              margin: "10px",
              padding: "10px",
            }}
          >
            <h3>{dealer.full_name}</h3>
            <p>{dealer.city}, {dealer.state}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Home;