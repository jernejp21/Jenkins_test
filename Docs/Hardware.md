---
layout: default
title: Hardware
nav_order: 2
---

# Hardware

## STM32MP157D-DK1 development board.

![Development board](../STM32MP157D-DK1.jpg)

To be able to use internal ADC, you will need to connect VREF+ to 3.3V. Either fit 0Ω resistor to R74, or connect IOREF (CN16, pin 2) to VREFP (CN13, pin 8).

This development board isn't fitted with Wi-Fi / Bluetooth module, so you will need ethernet cable. STM32MP157F-DK2 does have this module.

### Arduino connectors pinout

<table>
<thead>
  <tr>
    <th>Connector</th>
    <th>Pin name</th>
    <th>Signal name</th>
    <th>STM32 pin</th>
    <th>Comment</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="8">CN16</td>
    <td>1</td>
    <td>NC</td>
    <td>-</td>
    <td>NC</td>
  </tr>
  <tr>
    <td>2</td>
    <td>3V3</td>
    <td>-</td>
    <td>IOREF 3V3</td>
  </tr>
  <tr>
    <td>3</td>
    <td>NRST</td>
    <td>NRST</td>
    <td>NRST</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3V3</td>
    <td>-</td>
    <td>3V3</td>
  </tr>
  <tr>
    <td>5</td>
    <td>5V</td>
    <td>-</td>
    <td>5V</td>
  </tr>
  <tr>
    <td>6</td>
    <td>GND</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>7</td>
    <td>GND</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>8</td>
    <td>VIN</td>
    <td></td>
    <td>Not connected</td>
  </tr>
  <tr>
    <td rowspan="6">CN17</td>
    <td>1</td>
    <td>A0</td>
    <td>PF14</td>
    <td>ADC2_IN6</td>
  </tr>
  <tr>
    <td>2</td>
    <td>A1</td>
    <td>PF13</td>
    <td>ADC2_IN2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>A2</td>
    <td>ANA0</td>
    <td>ADC1_IN0, ADC2_IN0</td>
  </tr>
  <tr>
    <td>4</td>
    <td>A3</td>
    <td>ANA1</td>
    <td>ADC2_IN1, ADC1_IN1</td>
  </tr>
  <tr>
    <td>5</td>
    <td>A4</td>
    <td>PC3/PA12</td>
    <td>ADC1_IN13 (PC3)</td>
  </tr>
  <tr>
    <td>6</td>
    <td>A5</td>
    <td>PF12/PA11</td>
    <td>ADC1_IN6 (PF12)</td>
  </tr>
  <tr>
    <td rowspan="8">CN14</td>
    <td>1</td>
    <td>ARD_D0</td>
    <td>PE7</td>
    <td>USART7_RX</td>
  </tr>
  <tr>
    <td>2</td>
    <td>ARD_D1</td>
    <td>PE8</td>
    <td>USART7_TX</td>
  </tr>
  <tr>
    <td>3</td>
    <td>ARD_D2</td>
    <td>PE1</td>
    <td>IO</td>
  </tr>
  <tr>
    <td>4</td>
    <td>ARD_D3</td>
    <td>PD14</td>
    <td>TIM4_CH3</td>
  </tr>
  <tr>
    <td>5</td>
    <td>ARD_D4</td>
    <td>PE10</td>
    <td>IO</td>
  </tr>
  <tr>
    <td>6</td>
    <td>ARD_D5</td>
    <td>PD15</td>
    <td>TIM4_CH4</td>
  </tr>
  <tr>
    <td>7</td>
    <td>ARD_D6</td>
    <td>PE9</td>
    <td>TIM4_CH1</td>
  </tr>
  <tr>
    <td>8</td>
    <td>ARD_D7</td>
    <td>PD1</td>
    <td>IO</td>
  </tr>
  <tr>
    <td rowspan="10">CN13</td>
    <td>1</td>
    <td>ARD_D8</td>
    <td>PG3</td>
    <td>IO</td>
  </tr>
  <tr>
    <td>2</td>
    <td>ARD_D9</td>
    <td>PH6</td>
    <td>TIM12_CH1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>ARD_D10</td>
    <td>PE11</td>
    <td>SPI4_NSS and TIM1_CH2</td>
  </tr>
  <tr>
    <td>4</td>
    <td>ARD_D11</td>
    <td>PE14</td>
    <td>SPI4_MOSI and TIM1_CH4</td>
  </tr>
  <tr>
    <td>5</td>
    <td>ARD_D12</td>
    <td>PE13</td>
    <td>SPI4_MISO</td>
  </tr>
  <tr>
    <td>6</td>
    <td>ARD_D13</td>
    <td>PE12</td>
    <td>SPI4_SCK</td>
  </tr>
  <tr>
    <td>7</td>
    <td>GND</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>8</td>
    <td>VREFP</td>
    <td>-</td>
    <td>VREF+</td>
  </tr>
  <tr>
    <td>9</td>
    <td>ARD_D14</td>
    <td>PA12</td>
    <td>I2C5_SDA</td>
  </tr>
  <tr>
    <td>10</td>
    <td>ARD_D15</td>
    <td>PA11</td>
    <td>I2C5_SCL</td>
  </tr>
</tbody>
</table>

### Raspberry Pi connectors

<table>
<thead>
  <tr>
    <th>Function</th>
    <th>STM32 pin<br></th>
    <th>Pin</th>
    <th>Pin</th>
    <th>STM32 pin</th>
    <th>Function</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>3V3</td>
    <td>-</td>
    <td>1</td>
    <td>2</td>
    <td>-</td>
    <td>5V</td>
  </tr>
  <tr>
    <td>GPIO3 / I2C5_SDA</td>
    <td>PA12</td>
    <td>3</td>
    <td>4</td>
    <td>-</td>
    <td>5V</td>
  </tr>
  <tr>
    <td>GPIO3 / I2C5_SCL</td>
    <td>PA11</td>
    <td>5</td>
    <td>6</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>GPIO4 / MCO1</td>
    <td>PA8</td>
    <td>7</td>
    <td>8</td>
    <td>PB10</td>
    <td>GPIO14 / USART3_TX</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>-</td>
    <td>9</td>
    <td>10</td>
    <td>PB12</td>
    <td>GPIO15 / USART3_RX</td>
  </tr>
  <tr>
    <td>GPIO17 / USART3_RTS</td>
    <td>PG8</td>
    <td>11</td>
    <td>12</td>
    <td>PI5</td>
    <td>GPIO18 / SAI2_SCKA</td>
  </tr>
  <tr>
    <td>GPIO27 / SDMMC3_D3</td>
    <td>PD7</td>
    <td>13</td>
    <td>14</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>GPIO22 / SDMMC3_CK<br></td>
    <td>PG15</td>
    <td>15</td>
    <td>16</td>
    <td>PF1</td>
    <td>GPIO23 / SDMMC3_CMD</td>
  </tr>
  <tr>
    <td>3V3</td>
    <td>-</td>
    <td>17</td>
    <td>18</td>
    <td>PF0</td>
    <td>GPIO24 / SDMMC3_D0</td>
  </tr>
  <tr>
    <td>GPIO10 / SPI5_MOSI</td>
    <td>PF9</td>
    <td>19</td>
    <td>20</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>GPIO9 / SPI5_MISO</td>
    <td>PF8</td>
    <td>21</td>
    <td>22</td>
    <td>PF4</td>
    <td>GPIO25 / SDMMC3_D1</td>
  </tr>
  <tr>
    <td>GPIO11 / SPI5_SCK</td>
    <td>PF7</td>
    <td>23</td>
    <td>24</td>
    <td>PF6</td>
    <td>GPIO8 / SPI5_NSS</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>-</td>
    <td>25</td>
    <td>26</td>
    <td>PF3</td>
    <td>GPIO7</td>
  </tr>
  <tr>
    <td>I2C1_SDA</td>
    <td>PF15</td>
    <td>27</td>
    <td>28</td>
    <td>PD12</td>
    <td>I2C1_SCL</td>
  </tr>
  <tr>
    <td>GPIO5 / MCO2</td>
    <td>PG2</td>
    <td>29</td>
    <td>30</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>GPIO6 / TIM5_CH2</td>
    <td>PH11</td>
    <td>31</td>
    <td>32</td>
    <td>PD13</td>
    <td>GPIO12 / TIM4_CH2</td>
  </tr>
  <tr>
    <td>GPIO13 / TIM3_CH2</td>
    <td>PC7</td>
    <td>33</td>
    <td>34</td>
    <td>-</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>GPIO19 / SAI2_FSA</td>
    <td>PI7</td>
    <td>35</td>
    <td>36</td>
    <td>PB13</td>
    <td>GPIO16 / USART3_CTS</td>
  </tr>
  <tr>
    <td>GPIO26 / SDMMC3_D2</td>
    <td>PF5</td>
    <td>37</td>
    <td>38</td>
    <td>PI6</td>
    <td>DPIO20 / SAI2_SDA</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>-</td>
    <td>39</td>
    <td>40</td>
    <td>PF11</td>
    <td>GPIO21 / SAI2_SDB</td>
  </tr>
</tbody>
</table>

## Arduino CNC shield

**WARNING : do not supply 3V3, 5V from Arduino shield**


![Arduino CNC shield](../Arduino_CNC_Shield.jpg)

### CNC shield connection to STM32MP157D-DK1

Make sure you put on jumpers on D12/A.STP and D13/A.DIR, otherwise you will not be able to controll A-axis from microcontroller.

<table>
<thead>
  <tr>
    <th>Function</th>
    <th>STM32 pin<br></th>
    <th>CNC shield</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Enable all motors<br></td>
    <td>PG3</td>
    <td>EN</td>
  </tr>
  <tr>
    <td>X step</td>
    <td>PE1</td>
    <td>X.STEP</td>
  </tr>
  <tr>
    <td>X direction</td>
    <td>PD15</td>
    <td>X.DIR</td>
  </tr>
  <tr>
    <td>Y step<br></td>
    <td>PD14</td>
    <td>Y.STEP</td>
  </tr>
  <tr>
    <td>Y direction<br></td>
    <td>PE9</td>
    <td>Y.DIR</td>
  </tr>
  <tr>
    <td>Z step<br></td>
    <td>PE10</td>
    <td>Z.STEP</td>
  </tr>
  <tr>
    <td>Z direction<br></td>
    <td>PD1</td>
    <td>Z.DIR</td>
  </tr>
  <tr>
    <td>A step<br></td>
    <td>PE13</td>
    <td>A.STEP</td>
  </tr>
  <tr>
    <td>A direction<br></td>
    <td>PE12</td>
    <td>A.DIR</td>
  </tr>
  <tr>
    <td>X end stop<br></td>
    <td>PH6</td>
    <td>X.LIM</td>
  </tr>
  <tr>
    <td>Y end stop<br></td>
    <td>PE11</td>
    <td>Y.LIM</td>
  </tr>
  <tr>
    <td>Z end stop<br></td>
    <td>PE14</td>
    <td>Z.LIM</td>
  </tr>
  <tr>
    <td>Abort</td>
    <td>PF14</td>
    <td>Abort</td>
  </tr>
  <tr>
    <td>Hold</td>
    <td>PF13</td>
    <td>Hold</td>
  </tr>
  <tr>
    <td>Emergency stop<br></td>
    <td>NRST</td>
    <td>E-STOP</td>
  </tr>
  <tr>
    <td>UART7_TX</td>
    <td>PE8</td>
    <td>TX</td>
  </tr>
  <tr>
    <td>UART7_RX</td>
    <td>PE7</td>
    <td>RX</td>
  </tr>
  <tr>
    <td>SDA pin</td>
    <td>PA12</td>
    <td>SDA</td>
  </tr>
  <tr>
    <td>SCL pin</td>
    <td>PA11</td>
    <td>SCL</td>
  </tr>
</tbody>
</table>

## DIN rail adaptor

Because you will need to use both Arduino and Raspberry Pi connectors, it is difficult to place the board. So that we can use all the cables, you can 3D print this adaptor for DIN rail and make a connector converter, so all the pins are on bottom side of the board and you can lay the board on top side.

<!-- [Link to the model](https://www.printables.com/model/244705-din-clip-attachment-for-analog-discovery-2). -->

<!-- ![DIN adaptor](../picture.png) -->