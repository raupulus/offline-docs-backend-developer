---
title: '`zsensor`'
description: Zephyr sensor bindings
source_url: https://docs.micropython.org/en/latest/library/zephyr.zsensor.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/zephyr.zsensor.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1070
---

# `zsensor` --- Zephyr sensor bindings

zsensor

The `zsensor` module contains a class for using sensors with Zephyr.

## class Sensor --- sensor control for the Zephyr port

Use this class to access data from sensors on your board. See Zephyr documentation for sensor usage here: [Sensors](https://docs.zephyrproject.org/latest/reference/peripherals/sensor.html?highlight=sensor#sensors).

Sensors are defined in the Zephyr devicetree for each board. The quantities that a given sensor can measure are called a sensor channels. Sensors can have multiple channels to represent different axes of one property or different properties a sensor can measure. See [Channels](#channels) below for defined sensor channels. Each channel may have multiple attributes that can be changed and/or queried. See [Channel Attributes](#channel-attributes) below for defined sensor channel attributes.

### Constructor

Device names are defined in the devicetree for your board. For example, the device name for the accelerometer in the FRDM-k64f board is "FXOS8700".

### Methods

Sensor.measure()

Obtains a measurement sample from the sensor device using Zephyr sensor_sample_fetch and stores it in an internal driver buffer as a useful value, a pair of (integer part of value, fractional part of value in 1-millionths). Returns none if successful or OSError value if failure.

Sensor.get_float(sensor_channel)

Returns the value of the sensor measurement sample as a float.

Sensor.get_micros(sensor_channel)

Returns the value of the sensor measurement sample in millionths. (Ex. value of `(1, 500000)` returns as `1500000`)

Sensor.get_millis(sensor_channel)

Returns the value of sensor measurement sample in thousandths. (Ex. value of `(1, 500000)` returns as `1500`)

Sensor.get_int(sensor_channel)

Returns only the integer value of the measurement sample. (Ex. value of `(1, 500000)` returns as `1`)

Sensor.attr_set(sensor_channel, channel_attribute, val1, \[val2\])

Set the given channel's attribute to the given value. `val1` may be a float, in which case `val2` is not given, or `val1` can be used for the value's integer part and `val2` for the value's fractional part in millionths.

Returns `None` if successful, or raises `OSError`.

Sensor.attr_get_float(sensor_channel, channel_attribute)

Returns the value of the sensor channel's attribute as a float.

Many sensors do not support this or any other of the `attr_get` methods.

Sensor.attr_get_micros(sensor_channel, channel_attribute)

Returns the value of the sensor channel's attribute in millionths. (Ex. value of `(1, 500000)` returns as `1500000`)

Sensor.attr_get_millis(sensor_channel, channel_attribute)

Returns the value of the sensor channel's attribute in thousandths. (Ex. value of `(1, 500000)` returns as `1500`)

Sensor.attr_get_int(sensor_channel, channel_attribute)

Returns only the integer value of the channel's attribute. (Ex. value of `(1, 500000)` returns as `1`)

### Channels

ACCEL_X

Acceleration on the X axis, in m/s^2.

ACCEL_Y

Acceleration on the Y axis, in m/s^2.

ACCEL_Z

Acceleration on the Z axis, in m/s^2.

ACCEL_XYZ

Pseudo-channel representing all three accelerometer axes. Used for `Sensor.attr_set` and the `Sensor.attr_get_xxx()` methods.

GYRO_X

Angular velocity around the X axis, in radians/s.

GYRO_Y

Angular velocity around the Y axis, in radians/s.

GYRO_Z

Angular velocity around the Z axis, in radians/s.

GYRO_XYZ

Pseudo-channel representing all three gyroscope axes. Used for `Sensor.attr_set` and the `Sensor.attr_get_xxx()` methods.

MAGN_X

Magnetic field on the X axis, in Gauss.

MAGN_Y

Magnetic field on the Y axis, in Gauss.

MAGN_Z

Magnetic field on the Z axis, in Gauss.

DIE_TEMP

Device die temperature in degrees Celsius.

PRESS

Pressure in kilopascal.

PROX

Proximity. Dimensionless. A value of 1 indicates that an object is close.

HUMIDITY

Humidity, in percent.

LIGHT

Illuminance in visible spectrum, in lux.

ALTITUDE

Altitude, in meters.

### Channel Attributes

ATTR_SAMPLING_FREQUENCY

Sensor sampling frequency, i.e. how many times a second the sensor takes a measurement.

ATTR_LOWER_THRESH

Lower threshold for trigger.

ATTR_UPPER_THRESH

Upper threshold for trigger.

ATTR_SLOPE_TH

Threshold for any-motion (slope) trigger.

ATTR_SLOPE_DUR

Duration for which the slope values needs to be outside the threshold for the trigger to fire.

ATTR_HYSTERESIS

ATTR_OVERSAMPLING

Oversampling factor.

ATTR_FULL_SCALE

Sensor range, in SI units.

ATTR_OFFSET

The sensor value returned will be altered by the amount indicated by offset: final_value = sensor_value + offset.

ATTR_CALIB_TARGET

Calibration target. This will be used by the internal chip's algorithms to calibrate itself on a certain axis, or all of them.

ATTR_CONFIGURATION

Configure the operating modes of a sensor.

ATTR_CALIBRATION

Set a calibration value needed by a sensor.

ATTR_FEATURE_MASK

Enable/disable sensor features.

ATTR_ALERT

Alert threshold or alert enable/disable.

ATTR_FF_DUR

Free-fall duration represented in milliseconds. If the sampling frequency is changed during runtime, this attribute should be set to adjust freefall duration to the new sampling frequency.

ATTR_BATCH_DURATION

Hardware batch duration in ticks.

ATTR_GAIN

ATTR_RESOLUTION
