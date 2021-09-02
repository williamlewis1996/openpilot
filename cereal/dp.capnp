using Cxx = import "./include/c++.capnp";
$Cxx.namespace("cereal");

using Java = import "./include/java.capnp";
$Java.package("ai.comma.openpilot.cereal");
$Java.outerClassname("dp");

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
  dpAllowGas @14 :Bool;
  dpFollowingProfileCtrl @15 :Bool;
  dpFollowingProfile @16 :UInt8;
  dpAccelProfileCtrl @17 :Bool;
  dpAccelProfile @18 :UInt8;
  dpGearCheck @19 :Bool;
  dpSpeedCheck @20 :Bool;
  dpUiDisplayMode @21 :UInt8;
  dpUiSpeed @22 :Bool;
  dpUiEvent @23 :Bool;
  dpUiMaxSpeed @24 :Bool;
  dpUiFace @25 :Bool;
  dpUiLane @26 :Bool;
  dpUiLead @27 :Bool;
  dpUiSide @28 :Bool;
  dpUiTop @29 :Bool;
  dpUiBlinker @30 :Bool;
  dpUiBrightness @31 :UInt8;
  dpUiVolume @32 :Int8;
  dpToyotaLdw @33 :Bool;
  dpToyotaSng @34 :Bool;
  dpToyotaCruiseOverride @35 :Bool;
  dpToyotaCruiseOverrideVego @36 :Bool;
  dpToyotaCruiseOverrideAt @37 :Float32;
  dpToyotaCruiseOverrideSpeed @38 :Float32;
  dpVwTimebombAssist @39 :Bool;
  dpIpAddr @40 :Text;
  dpCameraOffset @41 :Int8;
  dpPathOffset @42 :Int8;
  dpLocale @43 :Text;
  dpSrLearner @44 :Bool;
  dpSrCustom @45 :Float32;
  dpAppd @46 :Bool;
  dpMapd @47 :Bool;
}
