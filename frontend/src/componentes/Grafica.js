import React from 'react';
import { Line } from 'react-chartjs-2';
import Card from 'react-bootstrap/Card';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);
const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Variable de proceso',
      },
    },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
const data = {
    labels,
    datasets: [
      {
        label: 'Dataset 1',
        data: labels.map(() => Math.random()),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };


const Grafica = () => {
    return (
    <Card style={{ width: '40rem', height: '25rem' }}>
         <Card.Header>{'Titulo'}</Card.Header>
        <Card.Body>
        <Line options={options} data={data} /> 
        </Card.Body>
    </Card>
    );
};

export default Grafica;