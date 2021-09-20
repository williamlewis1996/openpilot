using Cxx = import "./include/c++.capnp";
$Cxx.namespace("cereal");

using Java = import "./include/java.capnp";
$Java.package("ai.comma.openpilot.cereal");
$Java.outerClassname("Dp");

@0xbfa7e645486440c7;

# dp.capnp: a home for deprecated structs

# dp
struct DragonConf {
  dpThermalStarted @0 :Bool;
  dpThermalOverheat @1 :Bool;
  dpAtl @2 :Bool;
  dpAtlOpLong @3 :Bool;
  dpDashcamd @4 :Bool;
  dpAutoShutdown @5 :Bool;
  dpAthenad @6 :Bool;
  dpUploader @7 :Bool;
  dpLateralMode @8 :UInt8;
  dpSignalOffDelay @9 :Float32;
  dpLcMinMph @10 :UInt8;
  dpLcAutoCont @11 :Bool;
  dpLcAutoMinMph @12 :UInt8;
  dpLcAutoDelay @13 :Float32;
  dpLaneLessModeCtrl @14 :Bool;
  dpLaneLessMode @15 :UInt8;
  dpAllowGas @16 :Bool;
  dpFollowingProfileCtrl @17 :Bool;
  dpFollowingProfile @18 :UInt8;
  dpAccelProfileCtrl @19 :Bool;
  dpAccelProfile @20 :UInt8;
  dpGearCheck @21 :Bool;
  dpSpeedCheck @22 :Bool;
  dpUiDisplayMode @23 :UInt8;
  dpUiSpeed @24 :Bool;
  dpUiEvent @25 :Bool;
  dpUiMaxSpeed @26 :Bool;
  dpUiFace @27 :Bool;
  dpUiLane @28 :Bool;
  dpUiLead @29 :Bool;
  dpUiSide @30 :Bool;
  dpUiTop @31 :Bool;
  dpUiBlinker @32 :Bool;
  dpUiBrightness @33 :UInt8;
  dpUiVolume @34 :Int8;
  dpToyotaLdw @35 :Bool;
  dpToyotaSng @36 :Bool;
  dpToyotaCruiseOverride @37 :Bool;
  dpToyotaCruiseOverrideVego @38 :Bool;
  dpToyotaCruiseOverrideAt @39 :Float32;
  dpToyotaCruiseOverrideSpeed @40 :Float32;
  dpVwTimebombAssist @41 :Bool;
  dpIpAddr @42 :Text;
  dpCameraOffset @43 :Int8;
  dpPathOffset @44 :Int8;
  dpLocale @45 :Text;
  dpSrLearner @46 :Bool;
  dpSrCustom @47 :Float32;
  dpAppd @48 :Bool;
  dpMapd @49 :Bool;
}