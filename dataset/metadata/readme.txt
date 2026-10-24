This data package was produced by and downloaded from the National Ecological Observatory Network (NEON). NEON is
funded by the National Science Foundation (Awards 0653461, 0752017, 1029808, 1138160, 1246537, 1638695, 1638696,
1724433) and managed cooperatively by Battelle. These data are provided under the terms of the NEON data policy at
https://www.neonscience.org/data-policy.

DATA PRODUCT INFORMATION
------------------------

ID: NEON.DOM.SITE.DP1.20033.001

Name: Nitrate in surface water

Description: In situ sensor-based nitrate concentration, available as fifteen minute  averages in surface water in lakes, wadeable and non-wadeable streams

NEON Science Team Supplier: Aquatic Instrument System

Abstract: Nitrate is measured using an optical sensor at the downstream (S2) sensor station in streams and on the buoy at lake and river sites. It is reported as a mean value from 20 measurements made during a sampling burst every 15 minutes. Some older data may have been processed as the mean value from 50 measurements, but as of late 2018, the algorithm was updated to 20 measurements and older data will eventually be re-processed to use 20 measurements.

Latency:
Data collected in any given month are published during the second full week of the following month.

Brief Design Description: The stream sensor stations measure PAR at water surface, water level, temperature, water quality, and at downstream stations, nitrate. The buoys are comprised of sensor sets which measure meteorological parameters over a water surface along with submerged sensors that measure physical and chemical parameters of the water. Some of these sensors are unique to the buoy subsystem and others are shared with other NEON subsystems, such as the wadeable stream sensor sets or terrestrial towers. Due to power, space, and data storage constraints on the buoy, the configuration of sensors deployed on a buoy may be different than those in other parts of NEON.

Brief Study Area Description: Upstream (S1) and downstream (S2) sensor stations are at all stream sites within NEON. Buoys (S1) will be deployed as a single station at all lake and large river (non-wadeable) sites within NEON.

Sensor(s): Seabird - SUNA V2 UV nitrate sensor

Keywords: buoy, lakes, nitrate (NO3-), nitrogen (N), nutrients, rivers, streams, surface water, surface water chemistry, water quality


QUERY INFORMATION
-----------------

Date-Time for Data Publication: 2025-12-09 00:29 (UTC)
Start Date-Time for Queried Data: 2018-05-11 00:00 (UTC)
End Date-Time for Queried Data: 2018-06-01 00:00 (UTC)

Site: BIGC
Geographic coordinates (lat/long datum): 
Domain: D17


DATA PACKAGE CONTENTS
---------------------

This folder contains the following documentation files:
- This readme file: NEON.D17.BIGC.DP1.20033.001.readme.20260123T000749Z.txt
- Machine-readable metadata file describing the data package: NEON.D17.BIGC.DP1.20033.001.EML.20180511-20180601.20260123T000749Z.xml.
This file uses the Ecological Metadata Language (EML) schema. Learn more about this specification and tools to parse
it at https://www.neonscience.org/about/faq.
- Science review flags: NEON.D17.BIGC.DP1.20033.001.science_review_flags.20251209T002912Z.csv
- Other related documents are available such as engineering specifications, field protocols, and data processing 
documentation. Please visit https://data.neonscience.org/data-products/DP1.20033.001 for more information.


This folder also contains 2 data files:
NEON.D17.BIGC.DP1.20033.001.102.100.015.NSW_15_minute.2018-05.basic.20251209T002912Z.csv - Nitrate in surface water summarized over 2 minutes from burst measurements taken every 15 minutes
NEON.D17.BIGC.DP1.20033.001.ais_maintenance.2018-05.basic.20251209T002912Z.csv - Information related to aquatic sensor and infrastructure maintenance

Basic download package definition: Includes the data product, summary statistics, expanded uncertainty, and final quality flag.

Expanded download package definition: Includes the basic package information plus quality metrics for all of the quality assessment and quality control analyses.


FILE NAMING CONVENTIONS
-----------------------

NEON data files are named using a series of component abbreviations separated by periods. File naming conventions
for NEON data files differ between NEON science teams. A file will have the same name whether it is accessed via
NEON's data portal or API. Please visit https://www.neonscience.org/data-formats-conventions for a full description
of the naming conventions.

ISSUE LOG
----------

This log provides a list of issues identified during data collection or processing, prior to publication
of this data package. For a more recent log, please visit this data product's detail page at
https://data.neonscience.org/data-products/DP1.20033.001.

Issue Date: 2024-10-01
Issue: Site was damaged by Sand Stone Fire, knocking out power and comms.  SUNA should still be internally logging, and once this data is manually downloaded and ingested into the data processing pipeline, this data will be made available.
    Date Range: 2024-08-02 to 2024-10-16
    Location(s) Affected: SYCA
Resolution Date: 2024-11-26
Resolution: Site resumed streaming following repairs.  Logged SUNA data from the period the site was offline still needs to be ingested, but the stream was dry for almost entire period and data will be quality flagged anyway.

Issue Date: 2023-08-17
Issue: Failing sensor was streaming intermittently.
    Date Range: 2023-08-12 to 2023-09-12
    Location(s) Affected: FLNT
    Date Range: 2024-02-15 to 2024-04-01
    Location(s) Affected: FLNT
Resolution Date: 2024-06-14
Resolution: Sensor was replaced.

Issue Date: 2023-01-26
Issue: Intermittent data.
    Date Range: 2023-08-16 to 2023-09-09
    Location(s) Affected: CARI
    Date Range: 2024-05-12 to 2024-05-13
    Location(s) Affected: CARI
Resolution Date: 2024-06-13
Resolution: Sensor was replaced.

Issue Date: 2023-12-26
Issue: Poor calibration.
    Date Range: 2022-08-17 to 2022-08-30
    Location(s) Affected: REDB
    Date Range: 2023-07-17 to 2023-08-14
    Location(s) Affected: WLOU
    Date Range: 2023-10-11 to 2023-11-08
    Location(s) Affected: WLOU
Resolution Date: 2023-12-26
Resolution: SUNA recalibrated and affected data flagged.

Issue Date: 2022-08-17
Issue: High UV absorbance is causing the sensor algorithm for estimating nitrate concentration to be incorrect.  Comparison with grab samples indicates that the sensor-based measurements are significantly overestimated. We plan to look at the raw absorbance data and determine whether we can create our own algorithm for estimating nitrate concentration.  If data can be post-corrected, quality flags will be updated and a new log entry will be made.
    Date Range: 2018-05-01 to 2023-10-31
    Location(s) Affected: PRLA, PRPO
Resolution Date: 2023-10-31
Resolution: Affected data have been flagged.  Users may request raw absorbance data to attempt a post-correction on their own.

Issue Date: 2023-12-26
Issue: Erratic data likely due to ice and/or sediment in the optical window. Automated wiper was disabled to prevent damage while frozen under ice.
    Date Range: 2023-04-11 to 2023-04-18
    Location(s) Affected: CARI
    Date Range: 2023-10-10 to 2023-10-23
    Location(s) Affected: CARI
    Date Range: 2024-03-21 to 2024-06-13
    Location(s) Affected: CARI
    Date Range: 2024-04-24 to 2024-04-29
    Location(s) Affected: CARI
Resolution Date: 2023-04-18
Resolution: Sensor could not be accessed for manual cleaning because it was frozen under ice. Issue eventually resolved on its own and affected data were quality flagged.

Issue Date: 2022-09-12
Issue: Severe flooding destroyed several roads into Yellowstone National Park in June 2022, making the YELL and BLDE sites inaccessible to NEON staff. Preventive and corrective maintenance were not able to be performed, nor was the annual exchange of sensors for calibration and validation. While automated quality control routines are likely to detect and flag most issues, users are advised to review data carefully.
    Date Range: 2022-06-12 to 2022-10-31
    Location(s) Affected: BLDE
Resolution Date: 2022-10-31
Resolution: Normal operations resumed on October 31, 2022, when the National Park Service opened a newly constructed road from Gardiner, MT to Mammoth, WY with minimal restrictions. For more details about data impacts, see Data Notification https://www.neonscience.org/impact/observatory-blog/data-impacts-neons-yellowstone-sites-yell-blde-due-catastrophic-flooding-0

Issue Date: 2022-07-20
Issue: Study reach shifted upstream.  Old upstream location became new downstream location.
    Date Range: 2022-02-03 to 2022-02-03
    Location(s) Affected: SYCA
Resolution Date: 2022-07-20
Resolution: sensorPositions file updated to reflect new locations.

Issue Date: 2022-04-14
Issue: Fouled sensor. Data suspect.
    Date Range: 2022-03-30 to 2022-04-11
    Location(s) Affected: REDB
Resolution Date: 2022-04-14
Resolution: Sensor was manually cleaned and bad data flagged.

Issue Date: 2020-11-03
Issue: Low flow conditions resulting in exposed sensors
    Date Range: 2020-10-06 to 2021-04-18
    Location(s) Affected: KING (HOR.VER: 101.100; 102.100)
    Date Range: 2020-10-19 to 2021-04-30
    Location(s) Affected: SYCA (HOR.VER: 101.100; 102.100)
    Date Range: 2021-07-23 to 2021-09-02
    Location(s) Affected: MCRA
Resolution Date: 2022-01-14
Resolution: Stage came back up and sensors re-submerged on their own.

Issue Date: 2021-02-23
Issue: Following the planned seasonal removal of the buoy sensors, data processing continued to run producing files containing only flags. The files containing only flags have been published for the months of 11/2020 and 12/2020.
    Date Range: 2020-11-01 to 2020-12-31
    Location(s) Affected: PRPO (HOR.VER: 103.100); PRLA (HOR.VER: 103.100); LIRO (HOR.VER: 103.100); CRAM (HOR.VER: 103.100)
Resolution Date: 2022-01-14
Resolution: NEON adjusted the expected date range of buoy deployments to prevent non-deployment months from being published.

Issue Date: 2022-01-06
Issue: Large shift outside typical range for site. Possible calibration error.
    Date Range: 2019-10-24 to 2019-10-31
    Location(s) Affected: WLOU
    Date Range: 2020-01-09 to 2020-01-21
    Location(s) Affected: WALK
    Date Range: 2020-03-04 to 2020-05-27
    Location(s) Affected: WALK
    Date Range: 2020-06-22 to 2020-07-27
    Location(s) Affected: WALK
    Date Range: 2021-10-25 to 2021-12-20
    Location(s) Affected: WALK
Resolution Date: 2022-01-06
Resolution: Data flagged.

Issue Date: 2022-01-18
Issue: Data were reprocessed to incorporate minor and/or isolated corrections to quality control thresholds, sensor installation periods, geolocation data, and manual quality flags.
    Date Range: 2013-01-01 to 2021-10-01
    Location(s) Affected: All
Resolution Date: 2022-01-01
Resolution: Reprocessed provisional data are available now.  Reprocess data previously included in RELEASE-2021 will become available when RELEASE-2022 is issued.

Issue Date: 2021-01-14
Issue: Safety measures to protect personnel during the COVID-19 pandemic resulted in reduced or canceled maintenance activities for extended periods at NEON sites. Data availability and/or quality may be negatively impacted during this time.

In addition, the annual refresh of sensors and data acquisition systems (DAS) did not occur according to the typical 1-year schedule for many sites. The annual refresh is where freshly calibrated and verified sensors and DAS replace the units in the field.
    Date Range: 2020-03-23 to 2021-12-31
    Location(s) Affected: ALL
Resolution Date: 2021-12-31
Resolution: NEON reviewed data from all sites and time periods potentially impacted by COVID-19 safety precautions to identify and manually flag suspect data that escaped automated quality tests. Suspect data are indicated by the final quality flag in the data files, which should be used to inform data filtering prior to use. 

Data during this time period should be treated as valid unless marked suspect by other quality flags. Data that are overdue for field calibrations are indicated by the validCalQF quality flag.

Issue Date: 2022-04-13
Issue: Sensor exposed to air.
    Date Range: 2021-07-14 to 2021-11-07
    Location(s) Affected: ARIK (HOR.VER: 102.100)
Resolution Date: 2021-11-07
Resolution: Water returned.

Issue Date: 2021-10-13
Issue: Sensor frozen in ice
    Date Range: 2017-12-07 to 2018-02-08
    Location(s) Affected: COMO
    Date Range: 2020-01-31 to 2020-02-14
    Location(s) Affected: COMO
    Date Range: 2020-12-08 to 2021-03-28
    Location(s) Affected: COMO
    Date Range: 2021-12-17 to 2022-01-01
    Location(s) Affected: COMO
Resolution Date: 2021-10-13
Resolution: Data flagged until ice melted and sensor was reading in liquid water again.

Issue Date: 2021-07-26
Issue: Wiper broken and sensor became fouled.
    Date Range: 2021-06-18 to 2021-07-14
    Location(s) Affected: BIGC
Resolution Date: 2021-07-26
Resolution: Manually cleaned and replaced with sensor with working wiper.

Issue Date: 2021-06-03
Issue: Sensors were removed from the stream as part of error diagnostic.
    Date Range: 2021-05-13 to 2021-05-24
    Location(s) Affected: ARIK
Resolution Date: 2021-06-03
Resolution: Data flagged.

Issue Date: 2021-06-01
Issue: Power failure during attempted calibration resulted in bad data.
    Date Range: 2021-05-18 to 2021-06-22
    Location(s) Affected: REDB
Resolution Date: 2021-06-01
Resolution: Bad data flagged. new calibration performed.

Issue Date: 2021-05-20
Issue: Light counts >65k. Lamp saturating detector.
    Date Range: 2021-03-25 to 2021-04-03
    Location(s) Affected: CUPE (102.100)
Resolution Date: 2021-05-20
Resolution: New SUNA installed. Affected data flagged.

Issue Date: 2020-01-02
Issue: Sensor buried.
    Date Range: 2019-09-27 to 2019-10-10
    Location(s) Affected: CUPE (HOR.VER: 102.100)
    Date Range: 2020-06-12 to 2020-09-11
    Location(s) Affected: ARIK
Resolution Date: 2021-03-10
Resolution: Sensor unburied and data flagged.

Issue Date: 2021-03-10
Issue: Persistent negative values.  Bad sensor or bad calibration.
    Date Range: 2019-07-05 to 2019-09-17
    Location(s) Affected: HOPB (HOR:102)
    Date Range: 2020-08-29 to 2020-11-11
    Location(s) Affected: MCRA
    Date Range: 2020-12-02 to 2021-02-02
    Location(s) Affected: MCRA
Resolution Date: 2021-03-10
Resolution: Sensor replaced and data flagged.

Issue Date: 2021-03-10
Issue: Aging SUNA lamp caused drift and high measurement variability.
    Date Range: 2020-12-16 to 2021-02-17
    Location(s) Affected: ARIK
Resolution Date: 2021-03-10
Resolution: SUNA replaced and data flagged.

Issue Date: 2021-03-10
Issue: Persistent negative values.  Bad sensor or bad calibration.
    Date Range: 2021-06-17 to 2021-06-26
    Location(s) Affected: MART (HOR:112)
Resolution Date: 2021-03-10
Resolution: Sensor replaced and data flagged.

Issue Date: 2021-03-03
Issue: SUNA not cleaned or calibrated for extended period of time due to site restrictions. Data drifted downward.
    Date Range: 2020-10-30 to 2021-02-16
    Location(s) Affected: TECR
Resolution Date: 2021-03-03
Resolution: Cleaned and calibrated when site access allowed.  Data flagged.

Issue Date: 2021-03-29
Issue: High flow event dislodged sensor infrastructure.
    Date Range: 2021-01-13 to 2021-01-14
    Location(s) Affected: MART (HOR.VER: 102.100)
Resolution Date: 2021-01-14
Resolution: Sensor removed from stream.

Issue Date: 2020-06-19
Issue: Sensor detached from infrastructure
    Date Range: 2020-05-31 to 2020-06-17
    Location(s) Affected: BLDE (HOR.VER: 102.100)
Resolution Date: 2020-10-19
Resolution: SUNA reinstalled.

Issue Date: 2020-10-16
Issue: SUNA nitrate sensor malfunction.
    Date Range: 2018-11-17 to 2019-02-01
    Location(s) Affected: KING (102.100)
Resolution Date: 2020-10-16
Resolution: SUNA instrument replaced.

Issue Date: 2020-10-16
Issue: SUNA wiper malfunction caused obstruction likely influencing sensor optics.
    Date Range: 2019-01-01 to 2019-03-05
    Location(s) Affected: ARIK (102.100)
Resolution Date: 2020-10-16
Resolution: SUNA instrument replaced.

Issue Date: 2020-06-10
Issue: All data were reprocessed with the most recent algorithms, quality control thresholds, and/or other metadata to improve overall data coverage and quality. Notes have been added to the logs of previously identified issues that have been corrected.
    Date Range: 2013-01-01 to 2020-06-10
    Location(s) Affected: All
Resolution Date: 2020-06-10
Resolution: Reprocessed data were published.

Issue Date: 2020-02-03
Issue: SUNA lamp malfunction prevented appropriate reference spectra updates.
    Date Range: 2018-11-11 to 2018-12-06
    Location(s) Affected: BARC (HOR.VER: 103.100)
Resolution Date: 2020-02-03
Resolution: Manual flagging applied

Issue Date: 2019-12-31
Issue: SUNA was not calibrated for extended period
    Date Range: 2017-02-01 to 2018-01-24
    Location(s) Affected: SUGG (HOR.VER: 103.100)
Resolution Date: 2019-12-31
Resolution: Field staff began calibrating SUNA

Issue Date: 2019-12-17
Issue: insufficient transmittance due to high turbidity
    Date Range: 2019-11-29 to 2019-11-30
    Location(s) Affected: SYCA (HOR.VER: 102.100)
Resolution Date: 2019-12-17
Resolution: Flood waters lowered

Issue Date: 2019-12-19
Issue: SUNA not calibrated for extended period
    Date Range: 2019-11-04 to 2019-11-27
    Location(s) Affected: REDB (HOR.VER: 102.100)
Resolution Date: 2019-11-27
Resolution: Power lost to site

Issue Date: 2019-11-20
Issue: Broken wiper resulted in excessive biofouling.
    Date Range: 2019-05-28 to 2019-09-30
    Location(s) Affected: BLUE (HOR.VER: 112.100)
    Date Range: 2019-06-03 to 2019-07-31
    Location(s) Affected: LECO (HOR.VER: 102.100)
    Date Range: 2019-09-09 to 2019-09-26
    Location(s) Affected: LEWI (HOR.VER: 102.100)
Resolution Date: 2019-11-20
Resolution: SUNA replaced.

Issue Date: 2019-11-14
Issue: Variability in SUNA logging configurations coupled with inappropriate processing algorithms caused errors in data averaging.
    Date Range: 2018-01-01 to 2019-10-25
    Location(s) Affected: ARIK (HOR.VER:102.100), BARC (HOR.VER:103.100 ), COMO (HOR.VER: 102.100), MAYF (HOR.VER: 102.100), MCDI (HOR.VER: 102.100), MCRA (HOR.VER: 102.100), POSE (HOR.VER: 102.100), PRIN (HOR.VER: 102.100), PRLA (HOR.VER: 103.100), PRPO (HOR.VER: 103.100), WLOU (HOR.VER: 102.100), WALK (HOR.VER: 102.100), SYCA (HOR.VER: 102.100)
    Date Range: 2018-01-01 to 2019-12-31
    Location(s) Affected: SUGG (HOR.VER: 103.100)
    Date Range: 2018-05-17 to 2019-10-25
    Location(s) Affected: REDB (HOR.VER: 102.100)
    Date Range: 2018-06-06 to 2019-10-25
    Location(s) Affected: CARI (HOR.VER:102.100)
    Date Range: 2018-06-14 to 2019-10-25
    Location(s) Affected: BLWA (HOR.VER: 103.100), TOMB (HOR.VER: 103.100)
    Date Range: 2018-09-02 to 2019-10-25
    Location(s) Affected: BLUE (HOR.VER: 102.100)
    Date Range: 2018-09-24 to 2019-10-25
    Location(s) Affected: BIGC (HOR.VER: 102.100), BLDE (HOR.VER:102.100)
    Date Range: 2018-10-01 to 2018-12-31
    Location(s) Affected: TECR (HOR.VER: 102.100)
    Date Range: 2019-01-01 to 2019-10-25
    Location(s) Affected: CRAM (HOR.VER: 103.100), CUPE (HOR.VER: 102.100), FLNT  (HOR.VER: 103.100), GUIL (HOR.VER: 102.100), HOPB (HOR.VER: 102.100 & 112.100), LECO (HOR.VER: 102.100 & 112.100), LEWI (HOR.VER: 102.100), LIRO (HOR.VER: 103.100), TOOK (HOR.VER: 103.100), TECR (HOR.VER: 102.100)
    Date Range: 2019-01-01 to 2019-12-10
    Location(s) Affected: MART (HOR.VER: 102.100)
Resolution Date: 2019-11-14
Resolution: Configurations and algorithms were updated and data was reprocessed.

Issue Date: 2020-03-12
Issue: Buoy moved significantly down river while streaming data.
    Date Range: 2019-11-01 to 2019-11-03
    Location(s) Affected: TOMB (HOR.VER: 103.100)
Resolution Date: 2019-11-03
Resolution: Buoy stopped transmitting data

Issue Date: 2019-10-11
Issue: reference spectrum max light count > 55,000
    Date Range: 2019-09-30 to 2019-10-08
    Location(s) Affected: BLUE (HOR.VER: 112.100
Resolution Date: 2019-10-08
Resolution: Sensor removed, manual flagging added

Issue Date: 2019-08-26
Issue: Sensor possibly exposed to air
    Date Range: 2019-08-11 to 2019-08-23
    Location(s) Affected: PRIN (HOR.VER: 102.100)
    Date Range: 2019-08-24 to 2019-08-25
    Location(s) Affected: BLUE (HOR.VER: 112.100)
Resolution Date: 2019-08-25
Resolution: Sensor returned to water

Issue Date: 2019-06-18
Issue: SUNA lamp malfunctioning
    Date Range: 2019-04-01 to 2019-04-28
    Location(s) Affected: MCDI (HOR.VER: 102.100)
Resolution Date: 2019-05-04
Resolution: SUNA removed,  manual flagging added.

Issue Date: 2019-05-09
Issue: Incorrect calibration resulted in faulty data
    Date Range: 2019-03-22 to 2019-05-01
    Location(s) Affected: WALK (HOR.VER: 102.100)
    Date Range: 2019-06-06 to 2020-07-03
    Location(s) Affected: BARC (HOR.VER: 103.100)
    Date Range: 2020-02-04 to 2020-03-03
    Location(s) Affected: TECR (HOR.VER: 102.100)
    Date Range: 2021-10-28 to 2021-12-20
    Location(s) Affected: WALK (HOR.VER: 102.100)
Resolution Date: 2019-05-01
Resolution: New calibration performed.  Manual flagging added.

Issue Date: 2019-06-17
Issue: SUNA not cleaned or calibrated for extended period
    Date Range: 2019-03-05 to 2019-03-18
    Location(s) Affected: REDB (HOR.VER: 102.100)
Resolution Date: 2019-03-18
Resolution: SUNA calibrated, manual flagging applied.

Issue Date: 2019-06-19
Issue: SUNA not calibrated within 1 month
    Date Range: 2019-02-07 to 2019-03-04
    Location(s) Affected: GUIL (HOR.VER: 102.100)
Resolution Date: 2019-03-04
Resolution: SUNA replaced, manual flagging applied

Issue Date: 2019-02-19
Issue: Processing failures resulted in poor data product coverage for some sites and time periods.
    Date Range: 2018-01-01 to 2018-10-31
    Location(s) Affected: All locations.
Resolution Date: 2019-02-19
Resolution: Data reprocessed to improve data product coverage.

Issue Date: 2019-06-17
Issue: Sensor configured incorrectly
    Date Range: 2018-05-01 to 2019-01-28
    Location(s) Affected: BIGC (HOR.VER: 102.100)
Resolution Date: 2019-01-28
Resolution: Sensor replaced

Issue Date: 2018-12-03
Issue: Water level receded and SUNA nitrate sensor became at least partially exposed.
    Date Range: 2017-07-01 to 2017-11-01
    Location(s) Affected: POSE (HOR.VER: 102.100)
    Date Range: 2018-10-10 to 2018-11-01
    Location(s) Affected: KING (HOR.VER: 102.100)
    Date Range: 2020-09-11 to 2020-11-02
    Location(s) Affected: ARIK (HOR.VER: 102.100)
Resolution Date: 2018-12-03
Resolution: Manual flagging applied.

Issue Date: 2018-08-30
Issue: SUNA drifted outside of accuracy threshold
    Date Range: 2018-02-25 to 2018-04-11
    Location(s) Affected: BARC
Resolution Date: 2018-08-30
Resolution: Manual flagging applied. Sensor offline while site awaits repair.

Issue Date: 2018-04-11
Issue: SUNA removed from KING due to low water levels
    Date Range: 2017-09-19 to 2018-04-11
    Location(s) Affected: KING(102.100)
Resolution Date: 2018-04-11
Resolution: Sensor offline until reinstallation

Issue Date: 2018-04-05
Issue: S2 infrastructure was damaged due to flooding.
    Date Range: 2018-03-27 to 2018-03-28
    Location(s) Affected: CUPE (102.100)
    Date Range: 2018-10-13 to 2018-10-18
    Location(s) Affected: PRIN (HOR.VER: 102.100)
Resolution Date: 2018-04-05
Resolution: Manual flagging applied. Sensor offline while site awaits repair.

Issue Date: 2018-03-27
Issue: Infrastructure damage to S2 from high flow event and calibration not verified prior to site repair.
    Date Range: 2018-02-21 to 2018-03-22
    Location(s) Affected: PRIN (102.100)
Resolution Date: 2018-03-22
Resolution: Manual flagging applied. Sensor offline while site awaits repair.

Issue Date: 2018-01-18
Issue: SUNA removed from the water and streaming from the bank.
    Date Range: 2017-12-12 to 2017-12-28
    Location(s) Affected: MCRA
Resolution Date: 2017-12-28
Resolution: SUNA returned to water.

Issue Date: 2018-02-05
Issue: S2 submerged and sensor position altered due to infrastructure damage from high flow event. Data are still usable.
    Date Range: 2017-10-30 to 2017-11-07
    Location(s) Affected: HOPB
Resolution Date: 2017-11-07
Resolution: Sensor offline while site awaiting repairs.

Issue Date: 2020-11-20
Issue: SUNA only calibrated annually.  No field calibrations
    Date Range: 2010-01-01 to 2017-07-01
    Location(s) Affected: All Sites
Resolution Date: 2017-07-01
Resolution: Calibration procedure created


ADDITIONAL INFORMATION
----------------------




NEON DATA POLICY AND CITATION GUIDELINES
----------------------------------------

A citation statement is available in this data product's detail page at
https://data.neonscience.org/data-products/DP1.20033.001. Please visit https://www.neonscience.org/data-policy for
more information about NEON's data policy and citation guidelines.

DATA QUALITY AND VERSIONING
---------------------------

NEON data are initially published with a status of Provisional, in which updates to data and/or processing
algorithms will occur on an as-needed basis, and query reproducibility cannot be guaranteed. Once data are published
as part of a Data Release, they are no longer provisional, and are associated with a stable DOI.

To learn more about provisional versus released data, please visit
https://www.neonscience.org/data-revisions-releases.